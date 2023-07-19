from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
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
            for i in range(0, randint(0, self.M-1)):
                print(m, "это м1")
                for j in range(0, randint(0, self.M-1)):
                    print(m, "это м2")
                    if self.pole[i][j].mine == True:
                        print("was")
                        continue
                    else:
                        self.pole[i][j].mine = True
                        print("put")
                    m += 1
                    print(m)
    def show(self):
        for i in self.pole:
            print(list(map(self.oh(), i)))

    def oh(self):
        if i == True:
            return "*"
        else:
            return "#"

a = GamePole(5, 5)
a.show()
print(a)
