import cImage as image
import os

def getImageFileNames(path):
    """specify path to folder containing some images and get a list of all the image names."""
    setNames = []
    setFileNames = []
    included_ext = ['jpg', 'png', 'bmp']
    cleanSetList = [fn for fn in os.listdir(path)
                    if any(fn.endswith(ext) for ext in included_ext)]
    for set in cleanSetList:
        setString = ''
        setFileNames.append(set)
        for i in range(len(set) - 4):
            setString = setString + set[i]
        setNames.append(setString)
    return setNames, setFileNames

def removeWhite(imgPath):
    """ removes white space from image at imgPath & returns Image object """
    im = image.Image(imgPath)
    im_2 = Image.open(imgPath)
    c = []  #list of columns where last black is (maybe)
    r = []  #list of rows where the last black is
    width = im.getWidth()
    height = im.getHeight()
    for col in range(width):
        for row in range(height):
            p = im.getPixel(col,row)
            avg = (p[0] + p[1] + p[2]) / 3
            if avg < 150:
                c.append(col)
                r.append(row)
    x_left = min(c)
    x_right = max(c)
    y_down = min(r)
    y_up = max(r)

    box = (x_left, y_down, x_right, y_up)
    im_2 = im_2.crop(box)
    return im_2

def main():
    setFileList = getImageFileNames('/Users/jmacaskill/PycharmProjects/cardbot-sort/icons')[1]
    setList = getImageFileNames('/Users/jmacaskill/PycharmProjects/cardbot-sort/icons')[0]
    win = image.ImageWin()
    setImageList = []
    for set in setFileList:
        path = '/Users/jmacaskill/PycharmProjects/cardbot-sort/icons/' + set
        setImageList.append(removeWhite(path))
        removeWhite(path).save("/Users/jmacaskill/PycharmProjects/cardbot-sort/cropicons/" + set)
    win.exitonclick()
main()