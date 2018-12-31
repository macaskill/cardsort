import cImage as image
import numpy

import os

from read_set import getImgPath


sets = ['ALLIANCES', 'ANTIQUITIES', 'APOCALYPSE', 'ARABIAN NIGHTS', 'ARCHENEMY', 'AVACYN RESTORED', 'BATTLE FOR ZENDIKAR', 'BATTLE ROYAL BOX SET', 'BEATDOWN BOX SET', 'BETA', 'BETRAYERS OF KAMIGAWA', 'BORN OF THE GODS', 'CHAMPIONS OF KAMIGAWA', 'CHRONICLES', 'COLDSNAP', 'COMMANDER 2013', 'COMMANDER 2014', 'COMMANDER 2015', 'COMMANDER 2016', "COMMANDER'S ARSENAL", 'COMMANDER', 'CONSPIRACY TAKE THE CROWN', 'CONSPIRACY', 'DARK ASCENSION', 'DARKSTEEL', 'DD AJANI V NICOL', 'DD BLESSED V CURSED', 'DD DIVINE V DEMONIC', 'DD ELSPETH V KIORA', 'DD ELSPETH V TEZZERET', 'DD ELVES V GOBLINS', 'DD GARRUK V LILIANA', 'DD HEROES V MONSTERS', 'DD IZZET V GOLGARI', 'DD JACE V CHANDRA', 'DD JACE V VRASKA', 'DD KNIGHTS V DRAGONS', 'DD NISSA V OB NIX', 'DD PHYREXIA V COALITION', 'DD SORIN V TIBALT', 'DD SPEED V CUNNING', 'DD VENSER V KOTH', 'DD ZENDIKAR V ELDRAZI', 'DISSENTION', "DRAGON'S MAZE", "DRAGON'S OF TARKIR", 'ELDRITCH MOON', 'ETERNAL MASTERS', 'EVENTIDE', 'EXODUS', 'EXPEDITION', 'FALLEN EMPIRES', 'FATE REFORGED', 'FIFTH DAWN', 'FIFTH EDITION', 'FOURTH EDITION', 'FTV ANGELS', 'FTV ANNIHILATION', 'FUTURE SIGHT', 'GATECRASH', 'GUILDPACT', 'HOMELANDS', 'ICE AGE', 'INNISTRAD', 'INVASION', 'JOURNEY INTO NYX', 'JUDGEMENT', 'KALEDASH', 'KHANS OF TARKIR', 'LEGENDS', 'LEGIONS', 'LORWYN', 'M2010', 'M2011', 'M2012', 'M2013', 'M2014', 'M2015', 'MASTERPIECE', 'MERCADIAN MASQUES', 'MIRAGE', 'MIRRODIN BESIEGED', 'MIRRODIN', 'MODERN EVENT DECK', 'MODERN MASTERS 2015', 'MODERN MASTERS', 'MORNINGTIDE', 'NEMESIS', 'NEW PHYREXIA', 'OATH OF THE GATEWATCH', 'ODYSSEY', 'ONSLAUGHT', 'ORIGINS', 'PLANAR CHAOS', 'PLANECHASE 2012', 'PLANECHASE ANTHOLOGY', 'PLANECHASE', 'PLANESHIFT', 'PORTAL SECOND AGE', 'PORTAL THREE KINGDOMS', 'PORTAL', 'PROPHECY', 'RAVNICA', 'RETURN TO RAVNICA', 'REVISED', 'RISE OF THE ELDRAZI', 'SAVIORS OF KAMIGAWA', 'SCARS OF MIRRODIN', 'SCOURGE', 'SHADOWMOOR', 'SHADOWS OVER INNISTRAD', 'SHARDS OF ALARA', 'SIXTH EDITION', 'STARTER 1999', 'STARTER 2000', 'STRONGHOLD', 'TEMPEST', 'THE DARK', 'THEROS', 'TIME SPIRAL', 'TORMENT', 'UNGLUED', 'UNHINGED', 'UNLIMITED', "URZA'S DESTINY", "URZA'S LEGACY", "URZA'S SAGA", 'VANGUARD', 'VISIONS', 'WEATHERLIGHT', 'WORLDWAKE', 'ZENDIKAR']
#string of each MTG sets.
path = '/Users/jmacaskill/PycharmProjects/cardbot-sort/cropicons/'
#path to reference icons

def makeaDictionary(path):
    '''
    Specify a path, receive a dictionary of cImage files accessed by set name (key)
    :param path: path containing image files
    :return: dictionary of set Keys and cImage objects.
    '''
    dict = {}
    setNames = []
    included_ext = ['jpg', 'png', 'bmp']
    cleanSetList = [fn for fn in os.listdir(path)
                    if any(fn.endswith(ext) for ext in included_ext)]
    for set in cleanSetList:
        img = image.Image(path + set)
        set = set[:-4]
        dict[set] = img
    return dict

def stringtoCImage(str):
    str = str.upper()
    img = image.Image('cropicons/' + str + '.png')
    return img


def stringtoCVImage(str):
    '''
    input a string containing case-insensitive name of MTG set and receive corresponding cImage image
    object as imported from */cropicons
    :param str: name of MTG set, case insensitive
    :return: numpy array
    '''
    str = str.upper()
    img = cv2.imread('cropicons/' + str + '.png')
    return img

def expcImage(img):
    '''
    This function will take a cImage object and expand it to be double its original dimensions.
    :param img: cImage image object, A x B, png format.
    :return:  cImage image object, 2A x 2B, png format
    '''
    oldw = img.getWidth()
    oldh = img.getHeight()

    newim = image.EmptyImage(oldw * 2, oldh * 2)
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = img.getPixel(col, row)

            newim.setPixel(2*col, 2*row, oldpixel)
            newim.setPixel(2*col+1, 2*row, oldpixel)
            newim.setPixel(2*col, 2*row+1, oldpixel)
            newim.setPixel(2*col+1, 2*row+1, oldpixel)

    return newim

def sharpenStroke(img):
    '''
    Input a blurry greyscale cImage image object and receive one with enhanced blacks and normalized whites.
    :param img: cImage image object
    :return: cImage image object
    '''


def main():
    s = input("input name of set")
    path = getImgPath(s)
    img = stringtoCImage(s)
    img2 = stringtoCVImage(s)



main()