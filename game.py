from datetime import *

class Game:
    def __init__(self):
        self.alive = True
        self.points = 0
        self.snakeSize = 4
        self.gameDelay = 1.8

    def run(self):
        startTime = datetime.now()
        currentTime = datetime.now()
        while self.alive:
            elapsedSeconds = (currentTime - startTime).seconds/self.gameDelay
            if elapsedSeconds >= 1:
                startTime = currentTime
                print("Ha pasado un ciclo de reloj")
            currentTime = datetime.now()

g = Game()
g.run()