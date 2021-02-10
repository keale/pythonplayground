# -*- coding: utf-8 -*-
"""
Durchsucht alle Unterverzeichnisse und erstellt ein Directory,
mit Key = Filesize und Value = Array aus gleichgroßen Dateien

Im zweiten Schritt wird für die gleichgroße Dateien ein SHA256 Wert
ermittelt um die Gleichheit festzustellen. Die gleichen Dateien werden mit
Hash als Key in equalFiles gespeichert.
 
Created on Tue Dec 15 20:27:58 2020

@author: AlexK
alexander.kessler@uni-jena.de
"""

import hashlib
import os

dSizeAndFiles = {} #Beinhaltet ein Direktory mit Dateigröße als Key und entsprechende Liste der Dateien
equalFiles = {} #Dateien mit gleichem SHA Hash

#os.chdir("D:\Python")
os.chdir("C:\\Users\\AlexK\\work\\Fotos für Keppis Abschied")

for directory, subdirs, files in os.walk(".", topdown = True):
    for file in files:
        path = os.path.join(directory, file)
        size = os.path.getsize(path)
        if size in dSizeAndFiles:
            dSizeAndFiles[size] +=[path]
        else:
            dSizeAndFiles[size] = [path]
        
for key, files in dSizeAndFiles.items():
    if len(files) > 1:
        for file in files:
            h = hashlib.sha256(open(file,"rb").read()).hexdigest()
            if h in equalFiles:
                equalFiles[h] += [file]
            else:
                equalFiles[h] = [file]

