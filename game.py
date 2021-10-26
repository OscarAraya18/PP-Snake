from random import *
from datetime import *
from GUI import *

from keyboard import *

class Game:
    def __init__(self):
        self.GUI = GUI()

        self.alive = True
        self.pointDisplayed = False
        self.pointPosition = {"row":0, "column":0}

        self.points = 0

        self.snakeSize = 4
        self.snakeHead = {'column':1, 'row':4}
        self.snakeBody = [{'column':1, 'row':3},{'column':1, 'row':2}]
        self.snakeTail = {'column':1, 'row':1}

        self.gameDelay = 0.5

        self.keyPressed = ""

    def run(self):
        startTime = datetime.now()
        currentTime = datetime.now()
        while self.alive:
            elapsedSeconds = (currentTime - startTime).seconds/self.gameDelay
            if elapsedSeconds >= 1:
                self.placePoint()
                self.moveSnake()
                startTime = currentTime    
            currentTime = datetime.now()
            self.detectPlayerInput()


    def placePoint(self):
        if not self.pointDisplayed:
            column = randrange(0,30)
            row = randrange(0,30)
            self.GUI.drawPoint(column, row)
            self.pointDisplayed = True
            self.pointPosition["column"] = column
            self.pointPosition["row"] = row
        else:
            self.GUI.drawPoint(self.pointPosition["column"], self.pointPosition["row"])

    def moveSnake(self):
        if self.keyPressed == "Right":
            self.snakeBody = [{'column':self.snakeHead['column'], 'row':self.snakeHead['row']}] + self.snakeBody
            if self.snakeHead['row'] >= 30:
                self.snakeHead['row'] = 0
            else:
                self.snakeHead['row'] = self.snakeHead['row'] + 1
            self.GUI.drawSnake([self.snakeHead])
            self.GUI.deletePoint(self.snakeTail['column'], self.snakeTail['row'])
            self.snakeTail = self.snakeBody.pop()
        elif self.keyPressed == "Up":
            self.snakeBody = [{'column':self.snakeHead['column'], 'row':self.snakeHead['row']}] + self.snakeBody
            if self.snakeHead['column'] <= 0:
                self.snakeHead['column'] = 30
            else:
                self.snakeHead['column'] = self.snakeHead['column'] - 1
            self.GUI.drawSnake([self.snakeHead])
            self.GUI.deletePoint(self.snakeTail['column'], self.snakeTail['row'])
            self.snakeTail = self.snakeBody.pop()
        elif self.keyPressed == "Left":
            self.snakeBody = [{'column':self.snakeHead['column'], 'row':self.snakeHead['row']}] + self.snakeBody
            if self.snakeHead['row'] <= 0:
                self.snakeHead['row'] = 30
            else:
                self.snakeHead['row'] = self.snakeHead['row'] - 1
            self.GUI.drawSnake([self.snakeHead])
            self.GUI.deletePoint(self.snakeTail['column'], self.snakeTail['row'])
            self.snakeTail = self.snakeBody.pop()
        elif self.keyPressed == "Down":
            self.snakeBody = [{'column':self.snakeHead['column'], 'row':self.snakeHead['row']}] + self.snakeBody
            if self.snakeHead['column'] >= 30:
                self.snakeHead['column'] = 0
            else:
                self.snakeHead['column'] = self.snakeHead['column'] + 1
            self.GUI.drawSnake([self.snakeHead])
            self.GUI.deletePoint(self.snakeTail['column'], self.snakeTail['row'])
            self.snakeTail = self.snakeBody.pop()
        else:
            self.GUI.drawSnake([self.snakeHead])
            self.GUI.drawSnake([self.snakeTail])
            self.GUI.drawSnake(self.snakeBody)
    
    def detectPlayerInput(self):
        try:
            if is_pressed('left'):
                self.keyPressed = "Left"
            elif is_pressed('up'):
                self.keyPressed = "Up"
            elif is_pressed('right'):
                self.keyPressed = "Right"
            elif is_pressed('down'):
                self.keyPressed = "Down"
        except:
            pass 

