
import os
import os.path
import sys
file = input('Which data file do you want to use?')
if os.path.exists(file) == False:
    print('error ')
    sys.exit()
l=[]
f= open(file,'r')
for line in f:
    int_line = []
    for digit in line.split():
        int_line.append(int(digit))
    l.append(int_line)
a=int(input("How many decilitres of water do you want to pour down?"))

x = 0
h = float(0)
r = []
r1 = []
for i1 in range(len(l)):
    for j1 in range(len(l[i1])):
        r1.append(l[i1][j1])
        
for k in range(max(r1)+1):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == k:
                x += 1
    r.append(x)
    x = 0
##            if l[i][j] == 2:
##                y += 1
##            if l[i][j] == 3:
##                z += 1
##            if l[i][j] == 4:
##                p += 1
##            if l[i][j] == 5:
##                q += 1
ss = 0
for kk in range(len(r)):
    ss = ss + sum(r[0:kk])
for k1 in range(len(r)):
    #print('k1',k1)
    s = 0
    s1 = 0
    for k2 in range(1,k1+1):
        #print('k2',k2)
        s = s + sum(r[0:k2])
        #print('s',s)
    if a > ss:
        h = (a - ss) / ((i+1)*(j+1)) + len(r) - 1
        print('The water rises to {} centimetres.'.format("%.2f"%h))
        break
    else:
        if (a-s) < 0:
            for k3 in range(len(r)-1):
                s1 = s1 + sum(r[0:k3])
                
            h = (a-s1) / sum(r[0:k3+1]) + k1-1
            print('The water rises to {} centimetres.'.format("%.2f"%h))
            break
        if ((a - s) <= r[k1])and((a-s)>=0):
            #print('a-s',(a-s),sum(r[0:k1+1]))
            #print('k1',k1)
            h = (a-s) / sum(r[0:k1+1]) + k1
            print('The water rises to {} centimetres.'.format("%.2f"%h))
            break
##if a <= x:
##    h = a / x +1
##    print("%.2f"%h)
##else:
##    a = a - x
##    if a <= y:
##        h = a / (y+x) +2
##        print("%.2f"%h)
##    else :
##        a = a - (x+y)
##        if a <= z:
##            h = a / (x+y+z) +3
##            print("%.2f"%h)
##        else :
##            a = a - (x+y+z)
##            if a <= p:
##                h = a / (x+y+z+p) +4
##                print("%.2f"%h)
##            else :
##                a = a - (x+y+z+p)
##                if a <= q:
##                    h = a / (x+y+z+p+q) +5
##                    print("%.2f"%h)
##                else :
##                    h = 20
   
        
    
