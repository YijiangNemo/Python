# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint

from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def leftmost_longest_path_from_top_left_corner():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = ArrayQueue(10000)
    if (grid[0][0] == 0):
        return []
    q.enqueue([(0,0,0)])
    ans = []
    ansLength = 0
    while (len(q)>0):
        path = q.dequeue()
        if (len(path)>ansLength):
            ansLength = len(path)
            ans = path
        x,y,z = path[-1]
        zz = (z+1)%4
        for i in range(4):
            xx,yy = x+dx[zz],y+dy[zz]
            if (0<=xx<10 and 0<=yy<10 and grid[xx][yy]==1):
                flag = 0
                for x1,y1,z1 in path:
                    if (x1==xx and y1==yy):
                        flag = 1
                        break
                if (flag == 0):
                    tmp = path + [(xx,yy,zz)]
                    q.enqueue(tmp)
            zz = (zz+3)%4     
    result = []
    for x,y,z in ans:
        result.append((x,y))
    return result   



provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print('The leftmost longest path from the top left corner is {}'.format(path))
           
