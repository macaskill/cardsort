import json
raw_data = open("AllCards-x.txt", 'r')


# The last index will be when the string has 836 characters left, due to:
# len(""","legalities":[{"format":"Commander","legality":"Legal"},{"format":"Kaladesh Block","legality":"Legal"},{"format":"Legacy","legality":"Legal"},{"format":"Modern","legality":"Legal"},{"format":"Vintage","legality":"Legal"}]},"Tezzeret's Simulacrum":{"layout":"normal","name":"Tezzeret's Simulacrum","manaCost":"{3}","cmc":3,"type":"Artifact Creature — Golem","types":["Artifact","Creature"],"subtypes":["Golem"],"text":"{T}: Target opponent loses 1 life. If you control a Tezzeret planeswalker, that player loses 3 life instead.","power":"2","toughness":"3","imageName":"tezzeret's simulacrum","printings":["AER"],"legalities":[{"format":"Commander","legality":"Legal"},{"format":"Kaladesh Block","legality":"Legal"},{"format":"Legacy","legality":"Legal"},{"format":"Modern","legality":"Legal"},{"format":"Vintage","legality":"Legal"}]}}""")

cardSets = {}
string = ""

for aline in raw_data:
    string = string + str(aline)

raw_data.close()
end_string = string[len(string)-1000:len(string)+1]
def scrape(string):
    while len(string) > 100:
        index_i = string.index('"name') + 8
        index_f = string.index('","mana')
        name = string[index_i:index_f]
        if len(name) > 141:
            name = name[:name.index(',"')]
            print(name)
        string = string[index_f:]
        #now for the list of sets the card of given name was printed
        index_i = string.index('tings"') + 7
        index_f = string.index(',"legalities')
        strPrints = string[index_i:index_f]
        strPrints = strPrints[2:-2]
        lstPrints = strPrints.split('","')
        cardSets[name] = lstPrints
        string = string[index_f:]
        print(name, lstPrints)
        json.dump(cardSets, open("cardnames-test.txt", 'w'))

def refine(string):
    if string[-2:] == '''\"''':
        return string[:-2]

#to load a txt file formatted as a dictionary into python as a dictionary object:
cardSets = json.load(open("cardSetsReal.txt", 'r'), object_hook=dict)

for item in cardSets.items():
    if type(item) == tuple:
        cardSets[item[0]] = item[1]
        print(cardSets[item[0]])

json.dump(cardSets, open("cardSetsReal.txt", 'w'))


print(cardSets["Chaos Orb"])
print(len(cardSets))
#json.dump(cardSets, open("cardSetsReal.txt", 'w'))