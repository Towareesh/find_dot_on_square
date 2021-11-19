from math import sqrt, hypot


square = {'A': [0, 2], 'B': [2, 0], 'C': [-2, 0], 'D': [0, -2]}
dots_false = [[2, 2], [-3, 2], [-2.4, 0], [10, 40], [2.1, 2.1]]
dots_true  = [[-1, -1], [0, 0], [1, 1], [0.5, -0.5]]

def main(square, dot):

    null = square.get('A')
    nom_result = 0
    result = 0

    for i in 'BCD':
        nom_result += find_len(null, square.get(i))

    for n in 'ABCD':
        result += find_len(dot, square.get(n))

    if result <= nom_result:
        return True
    else:
        return False
    

    
def find_len(dot_1, dot_2):
    return hypot(dot_2[0] - dot_1[0], dot_2[1] - dot_1[1])

for i in dots_false:
    print(main(square, i))