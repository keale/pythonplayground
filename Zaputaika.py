# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:46:51 2021

@author: AlexK
"""

def swap_random(seq):
...     idx = range(len(seq))
...     i1, i2 = random.sample(idx, 2)
...     seq[i1], seq[i2] = seq[i2], seq[i1]

text = "Hallo world"
for word in text.split():
    if len(word)>2:
        i = 1
        while i < len(word) - 1 :
            word[i] = random 
            i += 1
    print(len(word))