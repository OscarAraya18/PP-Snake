from tkinter import *
from threading import *

class GUI(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def setupMainWindow(self):
        self.mainWindow.title('Snake')
        windowHeight = 604
        windowWidth = 604
        screeHeight = self.mainWindow.winfo_screenheight()
        screenWidth = self.mainWindow.winfo_screenwidth() 
        windowXPosition = (screenWidth/2) - (windowWidth/2)
        windowYPosition = (screeHeight/2) - (windowHeight/2)
        self.mainWindow.geometry('%dx%d+%d+%d' % (windowWidth,windowHeight,windowXPosition,windowYPosition))
        self.mainWindow.resizable(False,False)

    def drawGameGrid(self):
        for column in range(0,30):
            for row in range(0,30):
                if (row+column)%2==0:
                    self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray60", width=1)
                else:
                    self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray70", width=1)
        self.mainCanvas.pack(fill=BOTH, expand=1)


    def drawPoint(self, column, row):
        self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="#000", width=1, tags=str(column)+str(row))
    
    def deletePoint(self, column, row):
        if (row+column)%2==0:
            self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray60", width=1, tags=str(column)+str(row))
        else:
            self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray70", width=1, tags=str(column)+str(row))

    def drawSnake(self, positions):
        self.mainCanvas.delete("background")
        for position in positions:
            self.mainCanvas.create_rectangle(2 + 20*position['row'], 2 + 20*position['column'], 21 + 20*position['row'], 21 + 20*position['column'], 
            outline="#000", fill="green", width=1, tags=str(position['column'])+str(position['row']))

    def run(self):
        self.mainWindow = Tk()
        self.mainCanvas = Canvas(self.mainWindow)
        self.setupMainWindow()
        self.drawGameGrid()
        self.mainWindow.mainloop()