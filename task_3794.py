from math import sqrt, hypot


circle = [[0, 0], [2, 0]]
dots_false = [[2, 2], [-3, 2], [-2.4, 0], [10, 40], [2.1, 2.1]]
dots_true  = [[-1, 1], [0, 0], [1, 0], [0.5, -0.5], [0.2, 0.3]]

def IsPointInCircle(circle, dot):

    result = False
    dot_1 = circle[0]
    dot_2 = dot

    LenToDot = hypot(dot_2[0] - dot_1[0], dot_2[1] - dot_1[1])

    if LenToDot == circle[1][0]:
        result = True
        return result

for i in dots_true:
    print(IsPointInCircle(circle, i))