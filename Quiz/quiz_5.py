# Randomly fills an array of size 10x10 with 0s and 1s, and
# outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()

def check(i,j,nb):
##    if i < 2  and j< 2 :
##        print('y1')
##        print(grid)
##        if grid[i+2][j+1] == 1:
##            grid[i+2][j+1] = nb
##            return check(i+2,j+1,nb)
##        if grid[i+1][j+2] == 1:
##            grid[i+1][j+2] = nb
##            return check(i+1,j+2,nb)
##    if (i >= 2 and i <=8) and (j>=2 and j<=8):
##    print(i,j)
##    print('y')
##    print(grid)
    a = False
    b = False
    c = False
    d = False
    e = False
    f = False
    g = False
    h = False
    if i+2<=9 and j+1<=9 and (grid[i+2][j+1] == 1): 
        grid[i+2][j+1] = nb
        a = True
    if i+1<=9 and j+2<=9 and grid[i+1][j+2] == 1 :
        grid[i+1][j+2] = nb
        b = True
        
    if j-1>=0 and i-2>=0 and grid[i-2][j-1] == 1 :
        grid[i-2][j-1] = nb
        c = True
        
    if i-1>=0 and j-2>=0 and grid[i-1][j-2]== 1 :
        grid[i-1][j-2] = nb
        d = True
        
    if i-2>=0 and j+1<=9 and grid[i-2][j+1]== 1 :
        grid[i-2][j+1] = nb
        e = True
        
    if i-1>=0 and j+2<=9 and grid[i-1][j+2]== 1 :
        grid[i-1][j+2] = nb
        f = True
        
    if i+1<=9 and j-2>=0 and grid[i+1][j-2] == 1 :
        grid[i+1][j-2] = nb
        g = True
        
    if i+2<=9 and j-1>=0 and grid[i+2][j-1] == 1 :
        grid[i+2][j-1] = nb
        h = True
        
    if a ==True:
        check(i+2,j+1,nb)
    if b ==True:
        check(i+1,j+2,nb)
    if c ==True:
        check(i-2,j-1,nb)
    if d ==True:
        check(i-1,j-2,nb)
    if e ==True:
        check(i-2,j+1,nb)
    if f ==True:
        check(i-1,j+2,nb)
    if g ==True:
        check(i+1,j-2,nb)
    if h ==True:
        check(i+2,j-1,nb)
        

def explore_board():
    nb = 1
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == 1:
                nb += 1
                grid[i][j] = nb
                check(i,j,nb)
    nb_of_knights = nb - 1
    return nb_of_knights
##                print('nb',nb)
##                print(grid)
        
        
                
    
    


# Possibly insert extra code here


try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[None] * dim for _ in range(dim)]
if n > 0:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(n) > 0
else:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(-n) == 0
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
else:
    print('At least {} chess'.format(nb_of_knights), end = ' ')
    print('knight has', end = ' ') if nb_of_knights == 1 else print('knights have', end = ' ')
    print('explored this board.')

