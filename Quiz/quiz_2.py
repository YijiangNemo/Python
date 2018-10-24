# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by *** for COMP9021


from math import sqrt

def encode(a, b):

    s = 0
    if abs(a) > abs(b):
        
        if a >= 0:
            s = a * (4 *(a-1) +1) + b
        else:
            s = abs(a) * (4 *(abs(a)-1) +5) - b
    if abs(a) < abs(b):
        if b >= 0:
            s = b * (4 *(b-1) +3) - a
        else:
            s = abs(b) * (4 *(abs(b)-1) +7) + a
    if abs(a) == abs(b):
        if a >=0:
            if b>=0:
                s = a * (4 *(a-1) +1) + b
            else:
                s = a * (4 *a +4)
        else:
             s = abs(a) * (4 *(abs(a)-1) +5) - b

                
                
    return s
            
    # Replace pass above with your code

    
def decode(n):
    k = sqrt(n)
    if int(k) % 2 == 0:
        i = k // 2
        c = i *(4 *i +4) - n
        d = 1 + (i)*2
        if c+1 <= d:
            
            e = d/2 - 0.5 - c
            print((int(e),int(-i)))
            ##print('a')
        else:
            if c+2 <= 2*d:
                e = 3*d/2 -1.5 -c 
                print((int(-i),int(-e)))
                ##print('b')
    else:
        
        i = k // 2
        i = i + 1
        c = i *(4 *i +4) - n
        d = 1 + (i)*2
        if c+3 <= 3*d:
            
            e = c - (5*d/2 -2.5) 
            print((int(e),int(i)))
            
            ##print('c')
        else:
            e = (7*d/2 - 3.5) -c
            print((int(i),int(e)))
            ##print('d')
    
    # Replace pass above with your code
    

