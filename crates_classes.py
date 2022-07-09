from turtle import color


import random

class Attributes:
    item_painted = ['Black', 'Burnt Sienna', 'Cobalt', 'Crimson', 'Forest Green', 'Grey', 'Lime', 'Orange', 'Pink', 'Purple', 'Saffron', 'Sky Blue', 'Titanium White']
    item_certified = ['Acrobat', 'Aviator','Goalkeeper', 'Guradian', 'Juggler', 'Paragon', 'Playmaker', 'Scorer', 'Show-Off', 'Sniper', 'Striker', 'Sweeper', 'Tactician', 'Turtle', 'Victor']

class DragonLord(Attributes):
    
    def __init__(self):
        self.color = color
        self.certified 