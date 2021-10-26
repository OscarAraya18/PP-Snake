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
        self.sizeToGrow = 0

        self.snakeSize = 4
        self.snakeHead = {'column':1, 'row':4}
        self.snakeBody = [{'column':1, 'row':3},{'column':1, 'row':2}]
        self.snakeTail = {'column':1, 'row':1}

        self.gameDelay = 0.05

        self.keyPressed = ""



    def run(self):
        startTime = datetime.now()
        currentTime = datetime.now()
        while self.alive:
            elapsedSeconds = float((currentTime - startTime).microseconds/self.gameDelay)
            if elapsedSeconds >= 1.0:
                self.placePoint()
                self.moveSnake()
                self.growSnake()
                startTime = currentTime    
            currentTime = datetime.now()
            self.detectPlayerInput()


    def placePoint(self):
        if not self.pointDisplayed:
            availablePositions = []
            for column in range(0,30):
                for row in range(0,30):
                    availablePositions.append({'column':column, 'row':row})
            for snakePart in self.snakeBody:
                if snakePart in availablePositions:
                    availablePositions.remove(snakePart)
            if self.snakeHead in availablePositions:
                availablePositions.remove(self.snakeHead)
            if self.snakeTail in availablePositions:
                availablePositions.remove(self.snakeTail)

            shuffle(availablePositions)

            self.GUI.drawPoint(availablePositions[0]['column'], availablePositions[0]['row'])
            self.pointDisplayed = True
            self.pointPosition["column"] = availablePositions[0]['column']
            self.pointPosition["row"] = availablePositions[0]['row']
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
        self.detectPointCollision()
    
    def detectPlayerInput(self):
        try:
            if is_pressed('left') and not self.keyPressed == "Right":
                self.keyPressed = "Left"
            elif is_pressed('up') and not self.keyPressed == "Down":
                self.keyPressed = "Up"
            elif is_pressed('right') and not self.keyPressed == "Left":
                self.keyPressed = "Right"
            elif is_pressed('down') and not self.keyPressed == "Up":
                self.keyPressed = "Down"
        except:
            pass 

    
    def detectPointCollision(self):
        if self.snakeHead['column'] == self.pointPosition['column'] and self.snakeHead['row'] == self.pointPosition['row']:
            self.pointDisplayed = False
            self.points = self.points + 1
            self.sizeToGrow = self.sizeToGrow + 1
            self.gameDelay = self.gameDelay + 0.05
    
    def growSnake(self):
        if self.sizeToGrow > 0:
            availablePositions = []
            growToLeft = {'column': self.snakeTail['column'],'row': self.snakeTail['row']-1}
            if growToLeft not in self.snakeBody:
                availablePositions.append(growToLeft)
            growToUp = {'column': self.snakeTail['column']-1,'row': self.snakeTail['row']}
            if growToUp not in self.snakeBody:
                availablePositions.append(growToUp)
            growToRight = {'column': self.snakeTail['column'],'row': self.snakeTail['row']+1}
            if growToRight not in self.snakeBody:
                availablePositions.append(growToRight)
            growToDown = {'column': self.snakeTail['column']+1,'row': self.snakeTail['row']}
            if growToDown not in self.snakeBody:
                availablePositions.append(growToDown)

            if len(availablePositions) > 0:
                shuffle(availablePositions)
                self.snakeBody = self.snakeBody + [self.snakeTail]
                self.snakeTail = availablePositions[0]
                self.GUI.drawSnake([self.snakeTail])
                
                self.sizeToGrow = self.sizeToGrow - 1


