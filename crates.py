#Rare Item: 55%
#Very Rare Item: 28%
#Import Item: 12%
#Exotic Item: 4%
#Black Market Item: 1%
#Chance of receiving Painted attribute: 25%
#Chance of receiving Certified attribute: 25%

import random

def openCrate(rarity, painted, certified):

    crate_roll = []

    players_choice = {
        'Dragon Lord': [1, 'Decal', False, True],
        'Funny Book': [1, 'Decal', False, True],
        'Lone Wolf': [1, 'Decal', False, True],
        'StarLighter': [1, 'Decal', False, True],
        'Pearlescent Matte': [1, 'Paint Finish', False, True],

        'Chakram': [2, 'Wheels', True, True],
        'Reaper': [2, 'Wheels', True, True],
        'Gaiden': [2, 'Wheels', True, True],
        'Yamane': [2, 'Wheels', True, True],

        'Jäger 619 RS': [3, 'Body', True, True],
        'Twinzer': [3, 'Body', True, True],
        'Comet': [3, 'Rocket Boost', False, True],

        'Draco': [4, 'Wheels', True, True],
        'Zomba': [4, 'Wheels', True, True],
        'Infinium': [4, 'Wheels', True, True],

        'Dissolver': [5, 'Animated Decal', False, True],
        'Fire God': [5, 'Animated Decal', False, True],
        'Mainframe': [5, 'Animated Decal', False, True],
        'Solar Flare': [5, 'Goal Explosion', True, True],
    }

    item_painted = ['Black', 'Burnt Sienna', 'Cobalt', 'Crimson', 'Forest Green', 'Grey', 'Lime', 'Orange', 'Pink', 'Purple', 'Saffron', 'Sky Blue', 'Titanium White']
    item_certified = ['Acrobat', 'Aviator','Goalkeeper', 'Guradian', 'Juggler', 'Paragon', 'Playmaker', 'Scorer', 'Show-Off', 'Sniper', 'Striker', 'Sweeper', 'Tactician', 'Turtle', 'Victor']

    randItem = random.randint(1, 100)
    randPainted = random.randint(1, 100)
    randCertified = random.randint(1, 100)

    roll = random.choice(rarity)
    rollPainted = random.choice(item_painted)
    rollCertified = random.choice(item_certified)
    crate_roll.append(roll)
    if painted <= 25:
        crate_roll.append(rollPainted)
        print(f'{roll}, PAINTED: {rollPainted}')
    elif certified <= 25:
        crate_roll.append(rollCertified)
        print(f'{roll}, CERTIFIED: {rollCertified}')
    elif painted <= 25 and certified <= 25:
        crate_roll.append(rollPainted)
        crate_roll.append(rollCertified)
        print(f'{roll}, PAINTED: {rollPainted}, CERTIFIED: {rollCertified}')
    else:
        print(f'{roll}')
    return crate_roll
