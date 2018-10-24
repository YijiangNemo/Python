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
    def find(x,y,max_p):
        max_p -= 1
        if y+1 <= len(grid[x]) -1 and grid[x][y+1] == max_p:
            p.append((x,y+1))
            find(x,y+1,max_p)
        if x+1 <= len(grid) -1 and grid[x+1][y] == max_p:
            p.append((x+1,y))
            find(x+1,y,max_p)
        if x-1 >= 0 and grid[x-1][y] == max_p:
            p.append((x-1,y))
            find(x-1,y,max_p)
        if y-1 >= 0 and grid[x][y-1] == max_p:
            p.append((x,y-1))
            find(x,y-1,max_p)     
    def run1(x,y,path,not_u,not_d,not_l,not_r):
##        if path == 26:
##            return
        print(path)
        u = False
        d = False
        l = False
        r = False
        path += 1

        if y+1 <= len(grid[x]) -1 and grid[x][y+1] >= 1 and ((x,y) not in not_r):
            not_l.append((x,y+1))
            
            if path > grid[x][y+1]:
                grid[x][y+1] = path
            r = True
##            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            
        if y-1 >= 0 and grid[x][y-1] >= 1 and ((x,y) not in not_l):
            not_r.append((x,y-1))
            
            if path > grid[x][y-1]:
                grid[x][y-1] = path
            l = True
##            grid[x][y-1] = path
##            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            
        if x+1 <= len(grid) -1 and grid[x+1][y] >= 1 and ((x,y) not in not_d):
            not_u.append((x+1,y))
            
            if path > grid[x+1][y]:
                grid[x+1][y] = path
            d = True
##            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            


        if x-1 >= 0 and grid[x-1][y] >= 1 and ((x,y) not in not_u):
            not_d.append((x-1,y))
            
            if path > grid[x-1][y]:
                grid[x-1][y] = path
            u = True
##            grid[x-1][y] = path
##            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            

        if r == True:
            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            not_r.append((x,y))
        if l == True:
            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            not_l.append((x,y))
        if d == True:
            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            not_d.append((x,y))
        if u == True:
            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            not_u.append((x,y))
    def run2(x,y,path,not_u,not_d,not_l,not_r):
##        if path == 26:
##            return
        print(path)
        u = False
        d = False
        l = False
        r = False
        path += 1

        if x-1 >= 0 and grid[x-1][y] >= 1 and ((x,y) not in not_u):
            not_d.append((x-1,y))
            
            if path > grid[x-1][y]:
                grid[x-1][y] = path
            u = True
##            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            
        if x+1 <= len(grid) -1 and grid[x+1][y] >= 1 and ((x,y) not in not_d):
            not_u.append((x+1,y))
            
            if path > grid[x+1][y]:
                grid[x+1][y] = path
            d = True
##            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            
        if y+1 <= len(grid[x]) -1 and grid[x][y+1] >= 1 and ((x,y) not in not_r):
            not_l.append((x,y+1))
            
            if path > grid[x][y+1]:
                grid[x][y+1] = path
            r = True
##            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            
            

        if y-1 >= 0 and grid[x][y-1] >= 1 and ((x,y) not in not_l):
            not_r.append((x,y-1))
            
            if path > grid[x][y-1]:
                grid[x][y-1] = path
            l = True
##            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            


        if u == True:
            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            not_u.append((x,y))
        if d == True:
            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            not_d.append((x,y))
        if r == True:
            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            not_r.append((x,y))
        if l == True:
            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            not_l.append((x,y))

          

##    def run2(x,y,path):
##        path += 1
##        if x-1 >= 0 and grid[x-1][y] == 1:
##            grid[x-1][y] = path
##            run3(x-1,y,path)
##        if x+1 <= len(grid) -1 and grid[x+1][y] == 1:
##            grid[x+1][y] = path
##            run1(x+1,y,path)
##        if y+1 <= len(grid[x]) -1 and grid[x][y+1] == 1:
##            grid[x][y+1] = path
##            run2(x,y+1,path)
##        if y-1 >= 0 and grid[x][y-1] == 1:
##            grid[x][y-1] = path
##            run4(x,y-1,path)
    def run3(x,y,path,not_u,not_d,not_l,not_r):
##        if path == 26:
##            return
        print(path)
        path += 1
        u = False
        d = False
        l = False
        r = False

        if y-1 >= 0 and grid[x][y-1] >= 1 and ((x,y) not in not_l):
            not_r.append((x,y-1))
            
            if path > grid[x][y-1]:
                grid[x][y-1] = path
            l = True
##            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            
        if y+1 <= len(grid[x]) -1 and grid[x][y+1] >= 1 and ((x,y) not in not_r):
            not_l.append((x,y+1))
            
            if path > grid[x][y+1]:
                grid[x][y+1] = path
            r = True
##            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            
        if x-1 >= 0 and grid[x-1][y] >= 1 and ((x,y) not in not_u):
            not_d.append((x-1,y))
            
            if path > grid[x-1][y]:
                grid[x-1][y] = path
            u = True
##            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            
            


        if x+1 <= len(grid) -1 and grid[x+1][y] >= 1 and ((x,y) not in not_d):
            not_u.append((x+1,y))
            
            if path > grid[x+1][y]:
                grid[x+1][y] = path
            d = True
##            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            


        if l == True:
            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            not_l.append((x,y))
        if r == True:
            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            not_r.append((x,y))
        if u == True:
            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            not_u.append((x,y))

        if d == True:
            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            not_d.append((x,y))


##    def run3(x,y,path):
##        path += 1
##        if y-1 >= 0 and grid[x][y-1] == 1:
##            grid[x][y-1] = path
##            run4(x,y-1,path)
##        if y+1 <= len(grid[x]) -1 and grid[x][y+1] == 1:
##            grid[x][y+1] = path
##            run2(x,y+1,path)
##        if x-1 >= 0 and grid[x-1][y] == 1:
##            grid[x-1][y] = path
##            run3(x-1,y,path)
##        if x+1 <= len(grid) -1 and grid[x+1][y] == 1:
##            grid[x+1][y] = path
##            run1(x+1,y,path)

    def run4(x,y,path,not_u,not_d,not_l,not_r):
##        if path == 26:
##            return
        print(path)
        path += 1
        u = False
        d = False
        l = False
        r = False
        if x+1 <= len(grid) -1 and grid[x+1][y] >= 1 and ((x,y) not in not_d):
            not_u.append((x+1,y))
            
            if path > grid[x+1][y]:
                grid[x+1][y] = path
            d = True
##            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            
        if x-1 >= 0 and grid[x-1][y] >= 1 and ((x,y) not in not_u):
            not_d.append((x-1,y))
            
            if path > grid[x-1][y]:
                grid[x-1][y] = path
            u = True
##            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            
        if y-1 >= 0 and grid[x][y-1] >= 1 and ((x,y) not in not_l):
            not_r.append((x,y-1))
            
            if path > grid[x][y-1]:
                grid[x][y-1] = path
            l = True
##            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            
        if y+1 <= len(grid[x]) -1 and grid[x][y+1] >= 1 and ((x,y) not in not_r):
            not_l.append((x,y+1))
            
            if path > grid[x][y+1]:
                grid[x][y+1] = path
            r = True
##            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            



        if d == True:
            run1(x+1,y,path,not_u,not_d,not_l,not_r)
            not_d.append((x,y))
        if u == True:
            run3(x-1,y,path,not_u,not_d,not_l,not_r)
            not_u.append((x,y))
        if l == True:
            run4(x,y-1,path,not_u,not_d,not_l,not_r)
            not_l.append((x,y))


        if r == True:
            run2(x,y+1,path,not_u,not_d,not_l,not_r)
            not_r.append((x,y))




    not_l = []
    not_r = []
    not_u = []
    not_d = []
                
    l = []
    longest = []
    longest1 = []
    path = 2
    p = []
    x = 0
    y = 0
    if grid[x][y] == 1:
        grid[x][y] = path
        run1(x,y,path,not_u,not_d,not_l,not_r)
    else:
        return p
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            l.append(grid[i][j])
    max_p = max(l)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == max_p:
                longest.append((i,j))
    #print(longest)
    if len(longest) != 1:
        
        for i in range(len(longest)):
            longest1.append(longest[i][1])
        max_y = max(longest1)
        longest1 = []
        for i in range(len(longest)):
            if longest[i][1] == max_y:
                longest1.append(longest[i])
        #print(longest1)
        if len(longest1) != 1:
            longest = max(longest1)
            p= [longest]
        else:
            longest = longest1
            p = longest
    else:
        p = longest
    #print(p)
    x = p[0][0]
    y = p[0][1]
    find(x,y,max_p)
    p.reverse()
    return p
            

##    def check():
##        if len(p) > len(longest):
##            longest = p
##            p = []
##            print(longest)
##            refresh()    



 

##            if y+1 <= len(grid[x]) and grid[x][y+1] != 0:
##                grid[x][y] = 0
##                y += 1
##                p.append((x,y))
##            else:
##                if x+1 <= len(grid) and grid[x+1][y] != 0:
##                    grid[x][y] = 0
##                    x += 1
##                    p.append((x,y))
##                else:
##                    if y-1 <= 0 and grid[x][y-1] != 0:
##                        grid[x][y] = 0
##                        y -= 1
##                        p.append((x,y))
##                    else:
##                        return p
    
    # Replace pass above with your code

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
           
