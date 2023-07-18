from random import randint

class Cell:
    def __init__(self,around_mines = 0,  mine = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(self.N)] for j in range(self.N)]
        self.init()




    def init(self):
        m = 0
        while m <= self.M:
            for i in self.pole in range(0, randint(0, self.M)):
                print(type(self.pole))
                for j in i in range(0, randint(0, self.M)):
                    if self.pole.mine:
                        continue
                    else:
                        self.pole.mine = True



    def show(self):
        pass

a = GamePole(5,5)
print(a)

