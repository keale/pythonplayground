# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:22:37 2022

@author: AlexK
"""
def multTable(maxNr):
    num = range(1,maxNr+1)
    line=str()
    for k in num:
        line =""
        for i in num:
            line = line + " " +str(i*k).rjust(4," ")
        print(line + "\n")
        
        
        
liste=[1,"hallo", "welt"]

# x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]

# x.sort(key= lambda tup : tup[0])
# print(x)

# x.sort(key= lambda tup : tup[1])
# print(x)


def mult(*xx):
    if len(xx) > 0 :
        product = 1
        for x in xx:
            product = product * x   
        return product
    else: return 0
    
    
mult(1,3,4)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
