import random

#Rare Item: 55%
#Very Rare Item: 28%
#Import Item: 12%
#Exotic Item: 4%
#Black Market Item: 1%
#Chance of receiving Painted attribute: 25%
#Chance of receiving Certified attribute: 25%

count = 25

class PlayersChoice():
    
    rare = ['Dragon Lord', 'Funny Book', 'Lone Wolf', 'StarLighter', 'Pearlescent Matte']
    veryRare = ['Chakram', 'Reaper', 'Gaiden', 'Yamane']
    imports = ['Jäger 619 RS', 'Twinzer', 'Comet']
    exotic = ['Draco', 'Zomba', 'Infinium']
    blackMarket = ['Dissolver', 'Fire God', 'Mainframe', 'Solar Flare']

    def painted():
        item_painted = ['Black', 'Burnt Sienna', 'Cobalt', 'Crimson', 'Forest Green', 'Grey', 'Lime', 'Orange', 'Pink', 'Purple', 'Saffron', 'Sky Blue', 'Titanium White']
        roll = random.choices(item_painted, weights=[2, 3, 3, 2, 6, 3, 6, 6, 6, 6, 6, 4, 1])
        return roll

    def certified():
        item_certified = ['Acrobat', 'Aviator','Goalkeeper', 'Guradian', 'Juggler', 'Paragon', 'Playmaker', 'Scorer', 'Show-Off', 'Sniper', 'Striker', 'Sweeper', 'Tactician', 'Turtle', 'Victor']
        roll = random.choices(item_certified)
        return roll

    itemRoll = random.randint(1, 100)
    paintedRoll = random.randint(1, 4)
    certifiedRoll = random.randint(1, 4)

    if itemRoll <= 55:
        rareItem = random.choices(rare)
        print(rareItem, itemRoll)
    elif itemRoll > 55 and itemRoll <= 83:
        veryRareItem = random.choices(veryRare)
        print(veryRareItem, itemRoll)
    elif itemRoll > 83 and itemRoll <= 95:
        importsItem = random.choices(imports)
        print(importsItem, itemRoll)
    elif itemRoll > 95 and itemRoll <= 99:
        exoticItem = random.choices(exotic)
        print(exoticItem, itemRoll)
    else:
        blackMarketItem = random.choices(blackMarket)
        print(blackMarketItem, itemRoll)

while count > 0:
    PlayersChoice()
    count -= 1