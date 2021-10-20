from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.mainCanvas = Canvas(self)

        self.setupMainWindow()
        self.drawGameGrid()
        self.mainloop()

    def setupMainWindow(self):
        self.title('Snake')
        windowHeight = 604
        windowWidth = 604
        screeHeight = self.winfo_screenheight()
        screenWidth = self.winfo_screenwidth()
        windowXPosition = (screenWidth/2) - (windowWidth/2)
        windowYPosition = (screeHeight/2) - (windowHeight/2)
        self.geometry('%dx%d+%d+%d' % (windowWidth,windowHeight,windowXPosition,windowYPosition))
        self.resizable(False,False)

    def drawGameGrid(self):
        for column in range(0,30):
            for row in range(0,30):
                if (row+column)%2==0:
                    self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray60", width=1)
                else:
                    self.mainCanvas.create_rectangle(2 + 20*row, 2 + 20*column, 21 + 20*row, 21 + 20*column, outline="#000", fill="gray70", width=1)


        self.mainCanvas.pack(fill=BOTH, expand=1)


main = MainWindow()