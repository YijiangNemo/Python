# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of blocks
# in the largest block construction, determined by rows of 1s that can be stacked
# on top of each other. 
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


def size_of_largest_construction():
    w = []
    j3 = 0
    j4 = 0
    for a in range(dim-1,-1,-1):
        ##print(a)
        for b in range(dim):
            ##print(b)
            if (grid[a][b] != 0) :
                ##print('yes')
                j3 += 1
                for c in range(a-1,-1,-1):
                    if grid[c][b] != 0:
                        j3 += 1
                    else:
                        j4 = j4 + j3
                        ##print('j4=',j4)
                        j3 = 0
                        
                        break
            else:
                j4 = j4 + j3
                j3 = 0
    
                w.append(j4)
                j4 = 0
                ##print(w)
            if b == dim-1:
                ##print('no')

                j4 = j4+j3
                j3 = 0
                w.append(j4)
                j4 = 0
    size_of_largest_construction = int(max(w))
    return size_of_largest_construction 

                
 


    
    # Replace pass above with your code


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    pass
    # Replace pass above with your code


            
try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest block construction has {} blocks.'.format(size_of_largest_construction()))  
