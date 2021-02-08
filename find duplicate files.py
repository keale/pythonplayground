# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:27:58 2020

@author: AlexK
"""

import hashlib
import os, time

os.chdir("D:\Python")
files_w_size = []
for directory, subdirs, files in os.walk(".", topdown = True):
    for file in files:
        files_w_size += (os.path.join(directory, file))
        print(os.path.join(directory, file))
        
    for d in subdirs:
        print(os.path.join(directory, d))

# =============================================================================
# filename = "DSC00069.JPG" #input("Enter the input file name: ")
# with open(filename,"rb") as f: # Read a file in binary mode
#     
#     starttime = time.perf_counter() 
#     for i in range(10000):
#         bytes = f.read() # read entire file as bytes
#         readable_hash = hashlib.sha256(bytes).hexdigest()
#     
#     timedif = -starttime + time.perf_counter()
#     print(timedif)
# =============================================================================