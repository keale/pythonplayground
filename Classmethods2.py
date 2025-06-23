# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:28:27 2022

@author: AlexK
"""
from pprint import pprint


class Shape(object):
    # this is an abstract class that is primarily used for inheritance defaults
    # here is where you would define classmethods that can be overridden by inherited classes
    def __init__(self):
        self.name="Shape"
    
    @classmethod
    def from_square(cls, square):
        # return a default instance of cls
        return cls()
    
    
    def show(self):
        pprint(vars(self))
        
    
class Square(Shape):
    def __init__(self, side=10):
        self.side = side

    @classmethod
    def from_square(cls, square):
        return cls(side=square.side)
    
    
    
    # def show(self):
    #     super(self)
    #     pprint(vars(self))

class Rectangle(Shape):
    def __init__(self, length=10, width=10):
        self.length = length
        self.width = width

    @classmethod
    def from_square(cls, square):
        return cls(length=square.side, width=square.side)
    
sq = Square(8)
# sq.show()

sh = Shape()
sh.show()

rechteck = Rectangle.from_square(sq)
rechteck.show()


