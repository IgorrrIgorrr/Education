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
        while m != self.M:
            k = randint(0, self.N - 1)
            j = randint(0, self.N - 1)
            if self.pole[k][j].mine:
                continue
            else:
                self.pole[k][j].mine = True
                m += 1

        z = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for a in range(self.N):
            for b in range(self.N):
                mines = sum(self.pole[a + x][b + y].mine for x, y in z if 0 <= a + x < self.N and 0 <= b + y < self.N)
                self.pole[a][b].around_mines = mines

    def show(self):
        for i in self.pole:
            # Это очень длинный вариант, гораздо лучше сделать через мэп!!!
            # print()
            # for j in i:
            #     if j.mine:
            #         if j.fl_open:
            #             print("*", end="   ")
            #         else:
            #             print("#", end="   ")
            #     else:
            #         if j.fl_open:
            #             print(j.around_mines, end="   ")
            #         else:
            #             print("#", end="   ")
            print(*map(lambda x: "#" if not x.fl_open else x.around_mines if not x.mine else "*", i))

pole_game = GamePole(10, 12)

pole_game.show()
