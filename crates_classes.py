import random

#Rare Item: 55%
#Very Rare Item: 28%
#Import Item: 12%
#Exotic Item: 4%
#Black Market Item: 1%
#Chance of receiving Painted attribute: 25%
#Chance of receiving Certified attribute: 25%

class PlayersChoice():
    
    rare = ['Dragon Lord', 'Funny Book', 'Lone Wolf', 'StarLighter', 'Pearlescent Matte']
    veryRare = ['Chakram', 'Reaper', 'Gaiden', 'Yamane']
    imports = ['Jäger 619 RS', 'Twinzer', 'Comet']
    exotic = ['Draco', 'Zomba', 'Infinium']
    blackMarket = ['Dissolver', 'Fire God', 'Mainframe', 'Solar Flare']
    item_painted = ['Black', 'Burnt Sienna', 'Cobalt', 'Crimson', 'Forest Green', 'Grey', 'Lime', 'Orange', 'Pink', 'Purple', 'Saffron', 'Sky Blue', 'Titanium White']
    item_certified = ['Acrobat', 'Aviator','Goalkeeper', 'Guradian', 'Juggler', 'Paragon', 'Playmaker', 'Scorer', 'Show-Off', 'Sniper', 'Striker', 'Sweeper', 'Tactician', 'Turtle', 'Victor']

    itemRoll = random.randint(1, 100)
    paintedRoll = random.randint(1, 4)
    certifiedRoll = random.randint(1, 4)

    if itemRoll <= 55:
        pass
    elif itemRoll > 55 and itemRoll <= 83:
        pass
    elif itemRoll > 83 and itemRoll <= 95:
        pass
    elif itemRoll > 95 and itemRoll <= 99:
        pass
    else:
        pass

    def item():
        pass

    def painted():
        pass

    def certified():
        pass