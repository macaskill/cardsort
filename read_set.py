import cv2
import numpy as np
import cImage as image
import os
from pprint import pprint


def getImgPath(SET):
    """inputting a set name and returning the path to the image"""
    SET = SET.upper()
    imgPath = "/Users/jmacaskill/PycharmProjects/cardbot-sort/cropicons/" + str(SET) + ".png"
    return imgPath

def getImageFileNames(path):
    """specify path to folder containing some images and get a list of all the image names."""
    setNames = []
    included_ext = ['jpg', 'png', 'bmp']
    cleanSetList = [fn for fn in os.listdir(path)
                    if any(fn.endswith(ext) for ext in included_ext)]
    for set in cleanSetList:
        setString = ''
        for i in range(len(set) - 4):
            setString = setString + set[i]
        setNames.append(setString)
    return setNames #returns a list of set names WITHOUT THE ASSOCIATED FILE EXTENSION

def main():
    """
    goal is to read the set from which a random MTG card originates...
    maybe lets start with which colour a card is lol
    """
    getImageFileNames('/Users/jmacaskill/PycharmProjects/cardbot-sort/cropicons')

#['ALLIANCES', 'ANTIQUITIES', 'APOCALYPSE', 'ARABIAN NIGHTS', 'ARCHENEMY', 'AVACYN RESTORED', 'BATTLE FOR ZENDIKAR', 'BATTLE ROYAL BOX SET', 'BEATDOWN BOX SET', 'BETA', 'BETRAYERS OF KAMIGAWA', 'BORN OF THE GODS', 'CHAMPIONS OF KAMIGAWA', 'CHRONICLES', 'COLDSNAP', 'COMMANDER 2013', 'COMMANDER 2014', 'COMMANDER 2015', 'COMMANDER 2016', "COMMANDER'S ARSENAL", 'COMMANDER', 'CONSPIRACY TAKE THE CROWN', 'CONSPIRACY', 'DARK ASCENSION', 'DARKSTEEL', 'DD AJANI V NICOL', 'DD BLESSED V CURSED', 'DD DIVINE V DEMONIC', 'DD ELSPETH V KIORA', 'DD ELSPETH V TEZZERET', 'DD ELVES V GOBLINS', 'DD GARRUK V LILIANA', 'DD HEROES V MONSTERS', 'DD IZZET V GOLGARI', 'DD JACE V CHANDRA', 'DD JACE V VRASKA', 'DD KNIGHTS V DRAGONS', 'DD NISSA V OB NIX', 'DD PHYREXIA V COALITION', 'DD SORIN V TIBALT', 'DD SPEED V CUNNING', 'DD VENSER V KOTH', 'DD ZENDIKAR V ELDRAZI', 'DISSENTION', "DRAGON'S MAZE", "DRAGON'S OF TARKIR", 'ELDRITCH MOON', 'ETERNAL MASTERS', 'EVENTIDE', 'EXODUS', 'EXPEDITION', 'FALLEN EMPIRES', 'FATE REFORGED', 'FIFTH DAWN', 'FIFTH EDITION', 'FOURTH EDITION', 'FTV ANGELS', 'FTV ANNIHILATION', 'FUTURE SIGHT', 'GATECRASH', 'GUILDPACT', 'HOMELANDS', 'ICE AGE', 'INNISTRAD', 'INVASION', 'JOURNEY INTO NYX', 'JUDGEMENT', 'KALEDASH', 'KHANS OF TARKIR', 'LEGENDS', 'LEGIONS', 'LORWYN', 'M2010', 'M2011', 'M2012', 'M2013', 'M2014', 'M2015', 'MASTERPIECE', 'MERCADIAN MASQUES', 'MIRAGE', 'MIRRODIN BESIEGED', 'MIRRODIN', 'MODERN EVENT DECK', 'MODERN MASTERS 2015', 'MODERN MASTERS', 'MORNINGTIDE', 'NEMESIS', 'NEW PHYREXIA', 'OATH OF THE GATEWATCH', 'ODYSSEY', 'ONSLAUGHT', 'ORIGINS', 'PLANAR CHAOS', 'PLANECHASE 2012', 'PLANECHASE ANTHOLOGY', 'PLANECHASE', 'PLANESHIFT', 'PORTAL SECOND AGE', 'PORTAL THREE KINGDOMS', 'PORTAL', 'PROPHECY', 'RAVNICA', 'RETURN TO RAVNICA', 'REVISED', 'RISE OF THE ELDRAZI', 'SAVIORS OF KAMIGAWA', 'SCARS OF MIRRODIN', 'SCOURGE', 'SHADOWMOOR', 'SHADOWS OVER INNISTRAD', 'SHARDS OF ALARA', 'SIXTH EDITION', 'STARTER 1999', 'STARTER 2000', 'STRONGHOLD', 'TEMPEST', 'THE DARK', 'THEROS', 'TIME SPIRAL', 'TORMENT', 'UNGLUED', 'UNHINGED', 'UNLIMITED', "URZA'S DESTINY", "URZA'S LEGACY", "URZA'S SAGA", 'VANGUARD', 'VISIONS', 'WEATHERLIGHT', 'WORLDWAKE', 'ZENDIKAR']

main()
