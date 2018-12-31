class Divide(Card):
    '''
    The idea here is to divide a rectangular data sample (numpy array) into N congruent rect sectors to make them
    easily accessible for analysis and hash compares.

    '''
    def __init__(self, row, col):
        '''
        With MTG cards various identifying attributes can be easily segregated by choosing row=col=3 and iterating over
        1-2 ninths (sFactor = 1/N for each attribute, though some attributes may call for 1/N < sFactor ≤ 2/N such as
        a card's name.
        :param img: numpy array img with outer black border cropped of a MTG card (width:height proportions are
                    important)
        :param row: density of sectors on the X axis.
        :param col: "                       " Y axis.
        '''
        super(Card, self).__init__()
        self.img = img
        self.row = row
        self.col = col

    def __str__(self):
        width = len(self.img[0])
        height = len(self.img)
        return str(width)+" by "+str(height)+" sectional with "+ str(self.row*self.col)+" sections of dimsenions "+str(width/self.row)+"px by "+str(height/self.col)+"px"

    def sector(self, X, Y):
        '''
        Returns an image as a numpy array that is at coordinate (X, Y), with 1,1 being the bottom left most.
        Assume for now the card is properly oriented
        :param X: X position
        :param Y: Y position
        :return: numpy array image
        '''
        img_sector = []

        #for i in range()

        return img_sector

