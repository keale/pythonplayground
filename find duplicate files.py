# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:27:58 2020

@author: AlexK
"""

import hashlib
import os

#os.chdir("D:\Python")
os.chdir("C:\\Users\\AlexK\\work\\Fotos für Keppis Abschied")
files_w_size = []
files_w_same_size = []
equalFiles = []
ssf = () #same size file

for directory, subdirs, files in os.walk(".", topdown = True):
    for file in files:
        path = os.path.join(directory, file)   #Dateipfad erzeugen
        files_w_size += [(path, os.path.getsize(path))] # Dateipfade mit Größe in Bytes
        
files_w_size.sort(key=lambda tup: tup[1]) #sortiere nach der Größe

#überprüfe benachbarte Elemente der nach Größe sortieren Liste
#Erzeuge Tuples mit Dateien der gleichen Größe
for file1, file2 in zip(files_w_size, files_w_size[1:]):
    if file1[1] == file2[1]:
        ssf += (file1,)
    else:
        ssf += (file1,)
        if len(ssf)>1:
            files_w_same_size += [ssf]
        ssf = ()



# for tpl in files_w_same_size:
#     for file1, file2 in zip(tpl,tpl[1:]):
#         print(file1, file2)
#         if  hashlib.sha256(open(file1[0],"rb").read()).hexdigest() == \
#             hashlib.sha256(open(file2[0],"rb").read()).hexdigest():
#             ssf += (file1,)
#         else:
#             ssf += (file1,)
#             if len(ssf)>1:
#                 equalFiles += [ssf]
#             ssf = ()

#     if len(ssf)>1:
#         equalFiles += [ssf]
        # ssf = ()
