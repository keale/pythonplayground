from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys, os 

MATRIX_SIZE = 3

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("tic_tac_toe.ui", self)
        
        self.btnMatrix = [[self.findChild(QPushButton, f'pushButton{x}{y}') for x in range(MATRIX_SIZE)] for y in range(MATRIX_SIZE)]
        self.lbl = self.findChild(QLabel,"label")
        self.btnStart=self.findChild(QPushButton, 'btnStart')
        self.counter = 0
        self.t="X"

        for x in range(MATRIX_SIZE):
            for y in range(MATRIX_SIZE):
                # lambda a, x=y  ... ist notwendig um early binding zu erzwingen. BG ist noch unklar...
                # Ansonsten bekommen alle Buttons die lambda des letzen Buttons 22
                # lambda wird verwendet, um aus einem clicker Pseudofunktionen für alle Buttons zu erzeugen.
                # Ansonsten hätte man für jeden Button eine eigene clicker methode gebraucht.
                self.btnMatrix[x][y].clicked.connect(lambda a, y=y, x=x: self.clicker(self.btnMatrix[x][y]))

        self.btnStart.clicked.connect(self.reset)

        self.show()

    def checkwon(self):
        won = False
        #Zeile, x = const
        for x in range(MATRIX_SIZE):
            row = [e.text() for e in self.btnMatrix[x]]
            # all() wendet eine Funktion auf alle Elemente an.
            # oft wird mit Operatoren verwendet, wie z.B. hier:
            won = all(t == self.t for t in row)
            if won: 
                return won   

        #Spalte y = const
        for y in range(MATRIX_SIZE):
            col = [ row[y].text() for row in self.btnMatrix ]
            won = all(e == self.t for e in col )
            if won: return won 
            
        # 1. Diagonale x = y
        d = [self.btnMatrix[x][x].text() for x in range(MATRIX_SIZE) ]
        won = all(e == self.t for e in d )
        if won: return won

        # 2. Diagonale x+y = 2
        d = [self.btnMatrix[x][2-x].text() for x in range(MATRIX_SIZE)]
        won = all(e == self.t for e in d )
        return won
    
    def clicker(self, btn):  
        btn.setText(self.t)
        btn.setEnabled(False)
        if self.checkwon(): 
            self.lbl.setText(f"{self.t} hat gewonnen!" )
            for row in self.btnMatrix:
                for btn in row:
                    btn.setEnabled(False)
        else:
            self.counter+=1
            self.t =  "X" if self.counter % 2 == 0 else "O"
            self.lbl.setText(f"{self.t} ist am Zug!" )
        
        
    
    def reset(self):
        for x in range(MATRIX_SIZE):
            for y in range(3):
                self.btnMatrix[x][y].setText("")
                self.btnMatrix[x][y].setEnabled(True)
        self.lbl.setText("X beginnt!")
        self.t="X"
        self.counter=0


app=QApplication(sys.argv)
UIWindow = UI()
app.exec_()