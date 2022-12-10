# --- Day 9: Rope Bridge ---
"""
>>> part_1([('R','4'), ('U','4'), ('L','3'), ('D','1'), ('R','4'), ('D','1'), ('L','5'), ('R','2')])
13
>>> follow((0, 1), (0, 0))
(0, 0)
>>> follow((0, 2), (0, 0))
(0, 1)
>>> follow((1, 2), (0, 1))
(0, 1)
>>> follow((2, 2), (2, 4))
(2, 3)
"""
from utils import read_file, distance

R = 0
C = 1


def follow(n1: tuple, n2: tuple) -> tuple:
    """
    """
    r, c = n2
    if n1[C] == n2[C] and n1[R] - n2[R] > 1:    # up
        r = n2[R] + 1
    elif n1[C] == n2[C] and n2[R] - n1[R] > 1:  # down
        r = n2[R] - 1
    elif n1[R] == n2[R] and n1[C] - n2[C] > 1:  # right
        c = n2[C] + 1
    elif n1[R] == n2[R] and n2[C] - n1[C] > 1:  # left
        c = n2[C] - 1
    elif abs(n1[C] - n2[C]) == 1 and n1[R] - n2[R] > 1:  # up right
        c = n1[C]
        r = n2[R] + 1
    elif abs(n1[C] - n2[C]) == 1 and n2[R] - n1[R] > 1:  # left down
        c = n1[C]
        r = n2[R] - 1
    elif abs(n1[R] - n2[R]) == 1 and n1[C] - n2[C] > 1:  # right up
        r = n1[R]
        c = n2[C] + 1
    elif abs(n1[R] - n2[R]) == 1 and n2[C] - n1[C] > 1:  # left down
        r = n1[R]
        c = n2[C] - 1
    return r, c


class Rope:
    h: tuple
    t: tuple
    head_moves: list
    tail_moves: list

    def __init__(self):
        self.h = (0, 0)
        self.t = (0, 0)
        self.head_moves = [(0, 0)]
        self.tail_moves = [(0, 0)]

    def _hold_move(self):
        self.head_moves.append(self.h)
        self.tail_moves.append(self.t)

    def move_r(self):
        self.h = (self.h[R], self.h[C] + 1)
        self.t = follow(self.h, self.t)
        self._hold_move()
        return self.h

    def move_l(self):
        self.h = (self.h[R], self.h[C] - 1)
        self.t = follow(self.h, self.t)
        self._hold_move()
        return self.h

    def move_u(self):
        self.h = (self.h[R] + 1, self.h[C])
        self.t = follow(self.h, self.t)
        self._hold_move()
        return self.h

    def move_d(self):
        self.h = (self.h[R] - 1, self.h[C])
        self.t = follow(self.h, self.t)
        self._hold_move()
        return self.h

    def count_tail_positions(self):
        return len(set(self.tail_moves))

    def print_tail(self):
        for i in range(10):
            for j in range(10):
                if (i, j) in self.tail_moves:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


def part_1(moves: list) -> int:
    r = Rope()
    for move in moves:
        match move:
            case "R", i:
                [r.move_r() for m in range(int(i))]
            case "L", j:
                [r.move_l() for m in range(int(j))]
            case "U", k:
                [r.move_u() for m in range(int(k))]
            case "D", h:
                [r.move_d() for m in range(int(h))]
    return r.count_tail_positions()


def part_2(moves: list) -> int:
    pass


if __name__ == "__main__":
    datas = read_file('../datas/d09.txt').split('\n')
    moves = list(map(lambda m: m.split(), datas))

    print(f"1: {part_1(moves)}")
    # print(f"2: {part_2(moves)}")
