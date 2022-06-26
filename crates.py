# Rare Item: 55%
# Very Rare Item: 28%
# Import Item: 12%
# Exotic Item: 4%
# Black Market Item: 1%
# Chance of receiving Painted attribute: 25%
# Chance of receiving Certified attribute: 25%

import random

def openCrate():

    crate_roll = []
    types = ['Decal', 'Animated Decal', 'Paint Finish', 'Body', 'Wheels', 'Rocket Boost', 'Trail', 'Goal Explosion']

    # weight: [name, type, paintable, certifiable]
    players_choice = {
        1: ['Dragon Lord', types[0], False, True],
        1: ['Funny Book', types[0], False, True],
        1: ['Lone Wolf', types[0], False, True],
        1: ['StarLighter', types[0], False, True],
        1: ['Pearlescent Matte', types[2], False, True],

        2: ['Chakram', types[4], True, True],
        2: ['Reaper', types[4], True, True],
        2: ['Gaiden', types[4], True, True],
        2: ['Yamane', types[4], True, True],

        3: ['Jäger 619 RS', types[3], True, True],
        3: ['Twinzer', types[3], True, True],
        3: ['Comet', types[5], False, True],

        4: ['Draco', types[4], True, True],
        4: ['Zomba', types[4], True, True],
        4: ['Infinium', types[4], True, True],

        5: ['Dissolver', types[1], False, True],
        5: ['Fire God', types[1], False, True],
        5: ['Mainframe', types[1], False, True],
        5: ['Solar Flare', types[7], True, True]
    }

    # weights = 1: 50%, 2: 35%, 3: 15%
    item_painted = { 
        1: 'Burnt Sienna',
        1: 'Cobalt',
        1: 'Sky Blue',
        1: 'Forest Green',
        2: 'Lime',
        2: 'Orange',
        2: 'Pink',
        2: 'Purple',
        2: 'Saffron',
        2: 'Grey',
        3: 'Crimson',
        3: 'Black',
        3: 'Titanium White'
    }
    
    item_certified = ['Acrobat', 'Aviator','Goalkeeper', 'Guradian', 'Juggler', 'Paragon', 'Playmaker', 'Scorer', 'Show-Off', 'Sniper', 'Striker', 'Sweeper', 'Tactician', 'Turtle', 'Victor']

    randItem = random.randint(1, 100)
    randPainted = random.randint(1, 100)
    randCertified = random.randint(1, 100)

    roll = random.choice(crate_roll)
    rollPainted = random.choice(item_painted)
    rollCertified = random.choice(item_certified)
    crate_roll.append(roll)
    
    if randPainted <= 25:
        crate_roll.append(rollPainted)
        print(f'{roll}, PAINTED: {rollPainted}')
    elif randCertified <= 25:
        crate_roll.append(rollCertified)
        print(f'{roll}, CERTIFIED: {rollCertified}')
    elif randPainted <= 25 and certified <= 25:
        crate_roll.append(rollPainted)
        crate_roll.append(rollCertified)
        print(f'{roll}, PAINTED: {rollPainted}, CERTIFIED: {rollCertified}')
    else:
        print(f'{roll}')
    return crate_roll
