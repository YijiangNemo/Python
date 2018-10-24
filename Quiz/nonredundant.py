import os
import os.path
import sys
import re
import random
from random import randint
from collections import deque
file = input('Which data file do you want to use?')
if os.path.exists(file) == False:
    print('Error:there is no file with that name')
    sys.exit()
l=deque()
f= open(file,'r')
for line in f.readlines():
    n = re.split(r'[R, () \n]',line)
    p = [int(n[2]),int(n[3])]
    l.append(p)
    
m=deque()
for i in range(len(l)):
    a = l[i][0]
    
    for i0 in range(len(l)):
        b = l[i0][1]
        if a == b:
            break
        if (a!=b) and (i0 == len(l)-1):
            m.append(a)
m = deque(set(m))
m3 = deque()
def check(l,m1):
    print('check',m1)
##    h = 1
##    for j1 in range(len(m1)):
##        if m1[j1][0]!= 0:
##            c = m1[j1][0]
##            h -= 1
##        
##        for j2 in range(len(m1)):
##            if (c == m1[j2][0]) and (c!= 0):
##                print(m1[j2])
##                h += 1
##                print('h',h)
    m11 = deque()
    for j1 in range(len(m1)):
        m11.append(m1[j1][0])
    for j2 in range(len(m11)):
        if 0 in m11:
            m11.remove(0)
    m12 = deque(set(m11))
    print('m112',m11,m12)
    if len(m12)<len(m11):
        #print('redun',h)
        for x1 in range(len(m12)):
            m11.remove(m12[x1])
            print('m11',m11)
        for x2 in range(len(m11)):
            c = m11[x2]
            for x in range(len(m1)):
                if m1[x][0] == c:
                    m3.append(m1[x])
                    print('m1',m1[x])
                    
                    m1[m1.index(m1[x])] = [0,0]
                    
                    #m1.remove([c,q])
                    return find(l,m1)
        #print(q,c)
        print(m1)
        
    else:
        #print('h',h)
        return find(l,m1) 

def find(l,m1):
    #print(m1)
    a = len(m1)
    for j in range(a):
        t = 0
        b = len(l)
        for jj in range(b):
            #print('j,jj',j,jj)
            if (l[jj][0] == m1[j][0]):
                m1.append([l[jj][1],l[jj][0]])
                #l[jj] = [ -1,-1 ]
                
                
                print('find2',m1)
                t += 1
            if jj == len(l)-1:
                #print('y')
                if t>0:
                    m1.remove(m1[j])
                    check(l,m1)
 
                #print('find',m1)
        
        
        #l.remove(l[jj])
        
        #return find(l,m1)
                          
                      
            
##            m.popleft()
##            m.append(l[j][1])
##            print(l[j])
##            l.remove(l[j])
##            return find(l,m)
m1 = deque()
for i1 in range(len(m)):
    m1 = deque()
    m1.append([m[i1],0])
    q = m[i1]
    find(l,m1)
for v in range(len(m3)):
    m3[v].reverse()
    if m3[v] in l:
        l.remove(m3[v])
    


        
