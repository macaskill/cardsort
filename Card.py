import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import imagehash
import pytesseract

class Point:
    '''
    Just a simple old point in 2-space.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, Point):
        '''
        calculates distance from self to specified Point object
        :param Point: Point object, like self.
        :return: float being distance between 2 points.
        '''
        x1, y1 = self.x, self.y
        x2, y2 = Point.getX(), Point.getY()
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

class Card():
    '''
    Returns a Card object. Operate on it in the following ways:
    type(Card(path).img) = numpy image array via scipy misc imread
    type(Card(path)) = __main__.Card
    '''
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.dim = self.img.shape
        self.y = self.dim[0]
        self.x = self.dim[1]

    def __str__(self):
        return ""+ str(self.x) +"px wide and " +str(self.y) + "px tall. "

    def show(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        plt.imshow(self.img)
        plt.show()

    def normalize(self):
        '''This method will be used to crop the outer border of a card's image file and return the result'''
        for i in range(4):
            while borderCheck(self.img[0]) == True:
                self.img = self.img[1:]
                if borderCheck(self.img[len(self.img)-1]) == True:
                    self.img = self.img[:len(self.img)-2]
            self.img = np.rot90(self.img)

        return self.img

    def blacken(self):
        '''gotta find where the edges are'''
        black_points = []
        thresh = 15  #threshold for darkening, may take some tweaking.
        for i in range(self.y):
            for j in range(self.x):
                if avg(self.img[i][j]) < thresh:
                    self.img[i][j] = np.zeros(3)
                    black_points.append((i,j))
        return self, black_points
        #niice, this first part finds the dark-ish places and makes them black.

class Sector():
    '''
    The idea here is to divide a rectangular data sample (numpy array) into N congruent rect sectors to make them
    easily accessible for analysis and hash compares.

    '''
    def __init__(self, img, row, col):
        '''
        With MTG cards various identifying attributes can be easily segregated by choosing row=col=3 and iterating over
        1-2 ninths (sFactor = 1/N for each attribute, though some attributes may call for 1/N < sFactor ≤ 2/N such as
        a card's name.
        :param img: numpy array img with outer black border cropped of a MTG card (width:height proportions are
                    important)
        :param row: density of sectors on the X axis.
        :param col: "                       " Y axis.
        '''
        self.img = img
        self.row = row
        self.col = col

    def __str__(self):
        width = len(self.img[0])
        height = len(self.img)
        return str(width) + " by " + str(height) + " sectional with " + str(
            self.row * self.col) + " sections of dimsenions " + str(width / self.row) + "px by " + str(
            height / self.col) + "px"

    def get(self, X, Y):
        '''
        Returns an image as a numpy array that is at coordinate (X, Y), with 1,1 being the Top left most.
        Assume for now the card is properly oriented
        :param X: X position
        :param Y: Y position
        :return: numpy array image
        '''
        width = len(self.img[0]) // self.row
        height = len(self.img) // self.col
        img_sector = self.img[int((height)*(X-1)):int(height*X), int(width*(Y-1)):int(width*Y)]
        return img_sector


def hash_img(img):
    img = Image.fromarray(img)
    hash = imagehash.average_hash(img)
    return hash

def avg(seq):
    avg = 0.0
    for i in range(len(seq)):
        avg = avg + seq[i]
    avg = avg / len(seq)
    return avg

def colourCheck(point):
    '''
    Boolean function that returns True if a pixel (point) is a 'useful' colour i.e. not black or white.
    :param point: sequence of length 3 representing RGB values at a point.
    :return: TRUE if useful colour, FALSE if not.
    '''
    sum = 0
    for value in point:
        sum = sum + value
    avg = sum/3
    if avg > 200: return False
    elif avg < 100: return False
    else: return True

def grayCheck(point):
    '''assuming point is a 3-tup type object, this returns true if it is a grayish point'''
    avg = 0.0
    for i in range(len(point)):
        avg = avg + point[i-1]
    avg = avg / 3
    threshold = 23

    for i in point:
        if avg >= i and avg - i < threshold:
            continue
        elif avg < i and i - avg < threshold:
            continue
        else: return False
    return True

def borderCheck(line):
    '''Checks to see if a given row is a border by colour checking each pixel and returning true if the
    same colourCheck result is received N = len(line) times'''
    # we assume Line is a numpy array containing 3-tups of RGB values for each point in a column of
    counter = 0
    thresh = 20  #make room for noise! wow <3 thresholds
    for p in line:
        if colourCheck(p) == False or grayCheck(p) == True:
            counter = counter + 1
            continue
    if len(line) - counter <= thresh:
        return True
    else:
        return False

def getColour(img, pos):
    '''
    returns a list (len3) representing the RGB values at specified coordinates x,y
    :param img: numpy.array
    :param pos: 2-tup, list of len-2 (x, y) where x: horizontal, y: vertical
    :return: list
    '''
    x, y = pos[0], pos[1]
    row = img[y]
    pixel = row[x]
    colour = []
    for i in pixel:
        colour.append(i)
    return colour


def main():
    '''NOTE: cv2.imread defaults to a BGR format img and pyplot expects RGB. if left unchanged, resulting
    display is blue images go to red, red images to blue and green more or less unchanged. '''
    path = "test/tes13.png"  #gonna be an issue with improperly cropped starting images. i.e. if there is
    setPath = "cropicons/DRAGON'S MAZE.png"
    # a colour outside of the black/white border of the card. i.e. tes11.png – however, tes12.png is perf
    testCard = Card(path)
    dMaze = Card(setPath)
    blackMana = Card("icons/manasym/black.png")
    # blackMana = misc.imread("icons/manasym/Bsm.png")
    # blackHash = hash_img(blackMana)
    # redMana = misc.imread("icons/manasym/Rsm.png")
    # redHash = hash_img(redMana)
    # greenMana = misc.imread("icons/manasym/Gsm.png")
    # greenHash = hash_img(greenMana)
    # whiteMana = misc.imread("icons/manasym/Wsm.png")
    # whiteHash = hash_img(whiteMana)
    # blueMana = misc.imread("icons/manasym/Usm.png")
    # blueHash = hash_img(blueMana)

    im = Card(path)
    im = Card.normalize(im)

    im_split = Sector(im, 5, 7)
    manaCost = Sector.get(im_split, 1, 5)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, 1, 3, 0, 0.04)
  #  dst = cv2.dilate(dst, None)
    im[dst>0.05*dst.max()]=[0,0,255]

    graySwamp = cv2.cvtColor(blackMana.img, cv2.COLOR_BGR2GRAY)
    dstSet = cv2.cornerHarris(graySwamp, 1, 3, 0, 0.04  )
    dstSet = cv2.dilate(dstSet, None)
    blackMana.img[dstSet > 0.05*dstSet.max()]=[0,0,255]

    plt.imshow(im)
    plt.show()
    im = Card(path)

    im = Card.normalize(im)
    imgDiv = Sector(im, 1, 7)  # Divide(image, desired # of COLUMNS, desired # of ROWS)
    cardName = imgDiv.get(1,1)
    cardName = cv2.cvtColor(cardName, cv2.COLOR_BGR2RGB)

    cardNameChopped = Sector(cardName, 7, 1)
    #(thresh, im_gray) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cardNameGray = cv2.cvtColor(cardName, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cardNameGray)
    plt.imshow(cardName)
    plt.show()
    txt = pytesseract.image_to_string(img)
    print(txt)


    # len(img) = height, so there are height # of width-length lists. or each i in range(0:height):
    # len(img[i]): width
main()