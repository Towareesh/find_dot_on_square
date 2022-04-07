from math import sqrt, hypot


square = {'A': [0, 1], 'B': [1, 0], 'C': [0, -1], 'D': [-1, 0]}
dots_false = [[2, 2], [-3, 2], [-2.4, 0], [10, 40], [2.1, 2.1]]
dots_true  = [[-1, 0], [0, 0], [1, 0], [0.5, -0.5], [0.2, 0.3]]


def dot_agree(x, y):

        b = False
        if x ** 2 + y ** 2 <= 2 ** (1/2):
            b = True
        return b

for i in dots_false:
    print(dot_agree(i[0], i[1]))