##Written by Yijiang Wu
##open txt file and store the number in l list
##use for loop to traverse l list to create the maze and store 'up','down','left'
##'right' four directions and number of the ways to go in l3 list
##inner point means no way to go
##l3_1,l3_2,l3_3 is base on l3 list to get different output
##use 7 kinds of check recursive function to modify these lists to simulate the maze
##the position of walls store in horizon and vertical list
##the position of dash shore in dash_h list which means horizon dash and dash_v list(vertical)
##use the method given by the hint on lecture to find the cul-de-sacs and store the position in list
import sys
from argparse import ArgumentParser
from re import sub
from statistics import mean
from itertools import count
import os
import copy
try:
    parser = ArgumentParser()
    parser.add_argument('--file', dest = 'filename',required = True)
    parser.add_argument('-print', dest = 'printer' ,action = 'store_true')
    args = parser.parse_args()
    file = args.filename
    if not os.path.exists(file):
        raise SystemExit
except SystemExit:
    print('There is no file named {} in the working directory, giving up...'.format(file))
    sys.exit()
#parser.parse_args('-print')


##if not os.path.exists(file):
##    print('There is no file named {} in the working directory, giving up...'.format(filename))
##    sys.exit()


#file = open(filename)
l = []
l1 = []
ll = []
##    with open(file) as f:
f = open(file,'r')
for line in f:
    int_line = []
    for c in line:
        if c.isdigit():
           int_line.append(int(c))
    if len(int_line) >= 1:
        l.append(int_line)

##check if the txt file is correct    
if len(l) < 2 or len(l) > 41:
    print('incorrect input')
    sys.exit
for i in range(len(l)):
    if len(l[i]) < 2 or len(l[i]) > 31:
            print('incorrect input')
            sys.exit
dash = []
dash_h = []
dash_v = []
horizon = []
vertical = []
areas = 0
gate = 0
wall = 0
path = 0
inner = []
inaccessible = []
cul = []
intersections = []
set_cul = 0
##function to output tex file
def f_write():
    for i in range(len(horizon)):
        if horizon[i][0] >= 0:
            f.write('    \draw (' + str(horizon[i][1]) +',' +str(horizon[i][0]) +') -- (' + str(horizon[i][2]) + ',' + str(horizon[i][0])+');\n')
    for i in range(len(vertical)):
        if vertical[i][0] >= 0:
            f.write('    \draw (' + str(vertical[i][0]) +',' +str(vertical[i][1]) +') -- (' + str(vertical[i][0]) + ',' + str(vertical[i][2])+');\n')
##        for j in range(len(l[i])):
##            if l[i][j] == 1:
##                f.write('    \draw (' + str(j) +',' +str(i) +') -- (' + str(j+1) + ',' + str(i)+');\n')
##            if l[i][j] == 2:
##                f.write('    \draw (' + str(j) +',' +str(i) +') -- (' + str(j) + ',' + str(i+1)+');\n')
##            if l[i][j] == 3:
##                f.write('    \draw (' + str(j) +',' +str(i) +') -- (' + str(j+1) + ',' + str(i)+');\n')
##                f.write('    \draw (' + str(j) +',' +str(i) +') -- (' + str(j) + ',' + str(i+1)+');\n')
    f.write('% Pillars\n')
    for i in range(len(pil)):
        x = pil[i][1]
        y = pil[i][0]
        f.write('    \\fill[green] (' + str(x) +',' + str(y) +') circle(0.2);\n')
    f.write('% Inner points in accessible cul-de-sacs\n')
    for i in range(len(cul_de)):
        x = cul_de[i][1]
        y = cul_de[i][0]
        f.write('    \\node at (' + str(x+0.5) +',' +str(y+0.5)+') {};\n')
    f.write('% Entry-exit paths without intersections\n')
    for i in range(len(dash_h)):
        if dash_h[i][0] >= 0:
            f.write('    \draw[dashed, yellow] (' + str(dash_h[i][1]+0.5) +','+str(dash_h[i][0]+0.5)+') -- ('+str(dash_h[i][2]+0.5)+','+str(dash_h[i][0]+0.5)+');\n')
    for i in range(len(dash_v)):
        if dash_v[i][0] >= 0:
            f.write('    \draw[dashed, yellow] (' + str(dash_v[i][0]+0.5) +','+str(dash_v[i][1]+0.5)+') -- ('+str(dash_v[i][0]+0.5)+','+str(dash_v[i][2]+0.5)+');\n')

##function to count the number of walls
def check():
    for x in range(len(keep)):
        if keep[x] >= 0:
            k = keep[x]
            keep[x] = -1
            for y in range(len(ll)):
                if ll[y][0] == k:
                    keep.append(ll[y][1])
                    ll[y] = [-1,-1]
                if ll[y][1] == k:
                    keep.append(ll[y][0])
                    ll[y] = [-1,-1]
            check()
##function to simulate the maze and store in l3
def check2(i1,j1):
    if 'u' in l3[i1][j1] and (i1-1 >=0):
        l3[i1][j1][0] = -1
        l3[i1][j1][1] = None
        l3[i1-1][j1][0] -= 1
        l3[i1-1][j1][2] = None
        return
        #check2(i1-1,j1)
    if 'd' in l3[i1][j1] and (i1+1 <= len(l3)-1):
        l3[i1][j1][0] = -1
        l3[i1][j1][2] = None
        l3[i1+1][j1][0] -= 1
        l3[i1+1][j1][1] = None
        return
 #      check2(i1+1,j1)
    if 'l' in l3[i1][j1] and (j1-1 >=0):
        l3[i1][j1][0] = -1
        l3[i1][j1][3] = None
        l3[i1][j1-1][0] -= 1
        l3[i1][j1-1][4] = None
        return
 #       check2(i1,j1-1)
    if 'r' in l3[i1][j1] and (j1+1 <= len(l3[0])-1):
        l3[i1][j1][0] = -1
        l3[i1][j1][4] = None
        l3[i1][j1+1][0] -= 1
        l3[i1][j1+1][3] = None
        return
 #       check2(i1,j1+1)
    return 
##Function to modify the inner list to get the number of inner point 
def check3(i1,j1,inner):
    if 'u' in l3_1[i1][j1] and (i1-1 >=0):
        l3[i1-1][j1][0] = 0
        l3_1[i1][j1][1] = None
        l3_1[i1-1][j1][0] -= 1
        l3_1[i1-1][j1][2] = None
        inner.append('1')
        check3(i1-1,j1,inner)
    if 'd' in l3_1[i1][j1] and (i1+1 <= len(l3)-1):
        l3[i1+1][j1][0] = 0
        l3_1[i1][j1][2] = None
        l3_1[i1+1][j1][0] -= 1
        l3_1[i1+1][j1][1] = None
        inner.append('1')
        check3(i1+1,j1,inner)
    if 'l' in l3_1[i1][j1] and (j1-1 >=0):
        l3[i1][j1-1][0] = 0
        l3_1[i1][j1][3] = None
        l3_1[i1][j1-1][0] -= 1
        l3_1[i1][j1-1][4] = None
        inner.append('1')
        check3(i1,j1-1,inner)
    if 'r' in l3_1[i1][j1] and (j1+1 <= len(l3[0])-1):
        l3[i1][j1+1][0] = 0
        l3_1[i1][j1][4] = None
        l3_1[i1][j1+1][0] -= 1
        l3_1[i1][j1+1][3] = None
        inner.append('1')
        check3(i1,j1+1,inner)
##function to count the number of cul
def check4(i1,j1):
    if 'u' in l3_1[i1][j1] and (i1-1 >=0) and ([i1-1,j1] in cul):
        l3_1[i1-1][j1][0] = -1
        l3_1[i1][j1][1] = None
        l3_1[i1-1][j1][0] -= 1
        l3_1[i1-1][j1][2] = None
        cul[cul.index([i1-1,j1])] = [-1,-1]
        check4(i1-1,j1)
    if 'd' in l3_1[i1][j1] and (i1+1 <= len(l3_1)-1) and ([i1+1,j1] in cul):
        l3_1[i1+1][j1][0] = -1
        l3_1[i1][j1][2] = None
        l3_1[i1+1][j1][0] -= 1
        l3_1[i1+1][j1][1] = None
        cul[cul.index([i1+1,j1])] = [-1,-1]
        check4(i1+1,j1)
    if 'l' in l3_1[i1][j1] and (j1-1 >=0) and ([i1,j1-1] in cul):
        l3_1[i1][j1-1][0] = -1
        l3_1[i1][j1][3] = None
        l3_1[i1][j1-1][0] -= 1
        l3_1[i1][j1-1][4] = None
        cul[cul.index([i1,j1-1])] = [-1,-1]
        check4(i1,j1-1)
    if 'r' in l3_1[i1][j1] and (j1+1 <= len(l3_1[0])-1) and ([i1,j1+1] in cul):
        l3_1[i1][j1+1][0] = -1
        l3_1[i1][j1][4] = None
        l3_1[i1][j1+1][0] -= 1
        l3_1[i1][j1+1][3] = None
        cul[cul.index([i1,j1+1])] = [-1,-1]
        check4(i1,j1+1)
##function to get the path with intersection and exclude it
def check5(i1,j1):
    if 'u' in l3_1[i1][j1] and (i1-1 >=0):
        l3[i1-1][j1][0] = -4
        l3_1[i1][j1][1] = None
        l3_1[i1-1][j1][0] -= 1
        l3_1[i1-1][j1][2] = None
        check5(i1-1,j1)
    if 'd' in l3_1[i1][j1] and (i1+1 <= len(l3)-1):
        l3[i1+1][j1][0] = -4
        l3_1[i1][j1][2] = None
        l3_1[i1+1][j1][0] -= 1
        l3_1[i1+1][j1][1] = None
        check5(i1+1,j1)
    if 'l' in l3_1[i1][j1] and (j1-1 >=0):
        l3[i1][j1-1][0] = -4
        l3_1[i1][j1][3] = None
        l3_1[i1][j1-1][0] -= 1
        l3_1[i1][j1-1][4] = None
        check5(i1,j1-1)
    if 'r' in l3_1[i1][j1] and (j1+1 <= len(l3[0])-1):
        l3[i1][j1+1][0] = -4
        l3_1[i1][j1][4] = None
        l3_1[i1][j1+1][0] -= 1
        l3_1[i1][j1+1][3] = None
        check5(i1,j1+1)
##function to count the number of path
def check6(i1,j1):
    if 'u' in l3_2[i1][j1] and (i1-1 >=0):
        l3_2[i1-1][j1][0] = -4
        l3_2[i1][j1][1] = None
        l3_2[i1-1][j1][0] -= 1
        l3_2[i1-1][j1][2] = None
        check6(i1-1,j1)
    if 'd' in l3_2[i1][j1] and (i1+1 <= len(l3_2)-1):
        l3_2[i1+1][j1][0] = -4
        l3_2[i1][j1][2] = None
        l3_2[i1+1][j1][0] -= 1
        l3_2[i1+1][j1][1] = None
        check6(i1+1,j1)
    if 'l' in l3_2[i1][j1] and (j1-1 >=0):
        l3_2[i1][j1-1][0] = -4
        l3_2[i1][j1][3] = None
        l3_2[i1][j1-1][0] -= 1
        l3_2[i1][j1-1][4] = None
        check6(i1,j1-1)
    if 'r' in l3_2[i1][j1] and (j1+1 <= len(l3_2[0])-1):
        l3_2[i1][j1+1][0] = -4
        l3_2[i1][j1][4] = None
        l3_2[i1][j1+1][0] -= 1
        l3_2[i1][j1+1][3] = None
        check6(i1,j1+1)
##function to count the number of accessible area
def check7(i1,j1):
    if 'u' in l3_3[i1][j1] and (i1-1 >=0):
        l3_3[i1][j1][0] = -4
        l3_3[i1][j1][1] = None
        l3_3[i1-1][j1][0] = -1
        l3_3[i1-1][j1][2] = None
        check7(i1-1,j1)
    if 'd' in l3_3[i1][j1] and (i1+1 <= len(l3_2)-1):
        l3_3[i1][j1][0] = -4
        l3_3[i1][j1][2] = None
        l3_3[i1+1][j1][0] = -1
        l3_3[i1+1][j1][1] = None
        check7(i1+1,j1)
    if 'l' in l3_3[i1][j1] and (j1-1 >=0):
        l3_3[i1][j1][0] = -4
        l3_3[i1][j1][3] = None
        l3_3[i1][j1-1][0] = -1
        l3_3[i1][j1-1][4] = None
        check7(i1,j1-1)
    if 'r' in l3_3[i1][j1] and (j1+1 <= len(l3_2[0])-1):
        l3_3[i1][j1][0] = -4
        l3_3[i1][j1][4] = None
        l3_3[i1][j1+1][0] = -1
        l3_3[i1][j1+1][3] = None
        check7(i1,j1+1)
n = len(l) + 1  
m = len(l[0]) +1  
k = 3 
l1 = [None]*n  
for i in range(len(l1)):  
    l1[i] = [0]*m   

for i in range(n):  
    for j in range(m):  
        l1[i][j] = [0]*k  
#print(l1)          
##n1 = len(l)  
##m1 = len(l[0]) 
## 
##l3 = [None]*n1  
##for i in range(len(l1)):  
##    l3[i] = [0]*m1   
##
##for i in range(n1):  
##    for j in range(m1):  
##        l1[i][j] = [4,'u','d','l','r'] 
for i in range(len(l)):
    for j in range(len(l[i])):
        #print(i,j)
        if l[i][j] == 1:
            horizon.append([i,j,j+1])
            ll.append([i*len(l[0]) + j,i*len(l[0]) + j + 1])
            l1[i][j][0] = l1[i][j][0] + 1
            l1[i][j+1][0] = l1[i][j+1][0] + 1
            l1[i][j][1] += 1 
            l1[i][j+1][1] += 1
           
        if l[i][j] == 2:
            #print('2',i,j)
            vertical.append([j,i,i+1])
            ll.append([i*len(l[0]) + j,(i+1)*len(l[0])+j])
            l1[i][j][0] += 1
            l1[i+1][j][0] += 1
            l1[i][j][2] += 1
            l1[i+1][j][2] += 1
        if l[i][j] == 3:
            horizon.append([i,j,j+1])
            vertical.append([j,i,i+1])
            ll.append([i*len(l[0]) + j,i*len(l[0]) + j + 1])
            ll.append([i*len(l[0]) + j,(i+1)*len(l[0])+j])
            l1[i][j][0] += 1
            l1[i][j+1][0] += 1
            l1[i][j][1] += 1
            l1[i][j+1][1] += 1
            l1[i][j][0] += 1
            l1[i+1][j][0] += 1
            l1[i][j][2] += 1
            l1[i+1][j][2] += 1
l2 = ll[:]

count_u = 0
count_d = 0
count_l = 0
count_r = 0
for a in range(len(l[0])):
    if l[0][a] != 0 :
        count_u += 1
    if l[len(l)-1][a] == 2:
        count_d += 1
    if l[len(l)-1][a] == 3:
        count_d += 1
if count_u >= 1:
    for a in range(len(l[0])):
        if l[0][a] == 0:
            gate += 1
        if l[0][a] == 2:
            gate += 1
else:
    for a in range(len(l[0])):
        if l[1][a] == 0:
            gate += 1
        if l[1][a] == 2:
            gate += 1
    gate = gate - 2

if count_d >= 1:
    gate = gate + len(l[len(l)-1])
else:
    gate = gate + len(l[len(l)-1]) -2
    for a in range(len(l[len(l)-2])):
        if l[len(l)-1][a] == 1:
            gate -= 1

for b in range(len(l)):
    if l[b][0] != 0:
        count_l += 1
    if l[b][len(l[b])-1] == 1:
        count_r += 1
    if l[b][len(l[b])-1] == 3:
        count_r += 1
if count_l >= 1:
    for b in range(len(l)):
        if l[b][0] == 0:
            gate += 1
        if l[b][0] == 1:
            gate += 1

else:
    for b in range(len(l)):
        if l[b][1] == 0:
            gate += 1
        if l[b][1] == 1:
            gate += 1
    gate = gate - 2

if count_r >= 1:
    gate = gate+len(l)
else:
    gate = gate+len(l) - 2
    for b in range(len(l)):
        if l[b][len(l[b])-1] == 2:
            gate -= 1
pillar = 0
pil = []
keep = []
for q in range(len(ll)):
    if ll[q][0] >= 0:
        #print('y',ll[q])
        wall += 1
        k = ll[q][0]
        keep.append(ll[q][1])
        ll[q] = [-1,-1]
        for q1 in range(len(ll)):
            if ll[q1][0] == k:
                keep.append(ll[q1][1])
                ll[q1] = [-1,-1]
        check()
            
if count_d < 1:
    if count_r < 1:
        l4 = [4,'u','d','l','r']
        ##l3 = copy.deepcopy(l)
        l3 = [([0]*(len(l[0])-1)) for i in range(len(l)-1)]
        for i in range(len(l3)):
            for j in range(len(l3[i])):
                l3[i][j] = copy.deepcopy(l4)

        for i in range(len(l3)):
            for j in range(len(l3[i])):
                if ([i*len(l[0]) + j,i*len(l[0]) + j + 1] or [i*len(l[0]) + j + 1,i*len(l[0]) + j])in l2:
                    l3[i][j][0] -= 1
                    l3[i][j][1] = None
                if ([(i+1)*len(l[0]) + j,(i+1)*len(l[0]) + j + 1] or [(i+1)*len(l[0]) + j + 1,(i+1)*len(l[0]) + j])in l2:
                    l3[i][j][0] -= 1
                    l3[i][j][2] = None
                if ([i*len(l[0]) + j,(i+1)*len(l[0])+j] or [(i+1)*len(l[0])+j,i*len(l[0]) + j]) in l2:
                    l3[i][j][0] -= 1
                    l3[i][j][3] = None
                if ([i*len(l[0]) + j+1,(i+1)*len(l[0])+j+1] or [(i+1)*len(l[0])+j+1,i*len(l[0]) + j+1]) in l2:
                    l3[i][j][0] -= 1
                    l3[i][j][4] = None
        l3_1 = copy.deepcopy(l3)
else:

    l4 = [4,'u','d','l','r']
    ##l3 = copy.deepcopy(l)
    l3 = [([0]*(len(l[0]))) for i in range(len(l))]
    for i in range(len(l3)):
        for j in range(len(l3[i])):
            l3[i][j] = copy.deepcopy(l4)

    for i in range(len(l3)):
        for j in range(len(l3[i])):
            if ([i*len(l[0]) + j,i*len(l[0]) + j + 1] or [i*len(l[0]) + j + 1,i*len(l[0]) + j])in l2:
                l3[i][j][0] -= 1
                l3[i][j][1] = None
            if ([(i+1)*len(l[0]) + j,(i+1)*len(l[0]) + j + 1] or [(i+1)*len(l[0]) + j + 1,(i+1)*len(l[0]) + j])in l2:
                l3[i][j][0] -= 1
                l3[i][j][2] = None
            if ([i*len(l[0]) + j,(i+1)*len(l[0])+j] or [(i+1)*len(l[0])+j,i*len(l[0]) + j]) in l2:
                l3[i][j][0] -= 1
                l3[i][j][3] = None
            if ([i*len(l[0]) + j+1,(i+1)*len(l[0])+j+1] or [(i+1)*len(l[0])+j+1,i*len(l[0]) + j+1]) in l2:
                l3[i][j][0] -= 1
                l3[i][j][4] = None
    l3_1 = copy.deepcopy(l3)
l3_3 = copy.deepcopy(l3)
for i in range(len(l1)-1):
    for j in range(len(l1[i])-1):
        if l1[i][j][0] == 0:
            pillar += 1
            pil.append([i,j])
for x in range(len(l[0])*len(l)):
    for i1 in range(len(l3)):
        for j1 in range(len(l3[i1])):
            if l3[i1][j1][0] == 1:
                check2(i1,j1)
for i in range(len(l3)):
    if l3[i][len(l3[i])-1][0] == 1:
        l3[i][len(l3[i])-1][0] = -1
    if l3[i][0][0] == 1:
        l3[i][0][0] = -1
for j in range(len(l3[0])):
    if l3[0][j][0] == 1:
        l3[0][j][0] = -1
    if l3[len(l3)-1][j][0] == 1:
        l3[len(l3)-1][j][0] = -1
for i2 in range(len(l3)):
    for j2 in range(len(l3[i])):
        if l3[i2][j2][0] == 0:
            inaccessible.append([i2,j2])
for i in range(len(inaccessible)):
    i1 = inaccessible[i][0]
    j1 = inaccessible[i][1]
    inner.append('1')
    check3(i1,j1,inner)
for i in range(len(l3)):
    for j in range(len(l3[i])):
        if l3[i][j][0] == -1:
            cul.append([i,j])
        if l3[i][j][0] > 2:
            intersections.append([i,j])
cul_de = copy.deepcopy(cul)
for x in range(len(cul)):
    if cul[x][0] >= 0:
        i = cul[x][0]
        j = cul[x][1]
        set_cul += 1
        cul[x] = [-1,-1]
        check4(i,j)
for x in range(len(intersections)):
    if intersections[x][0] >= 0:
        i1 = intersections[x][0]
        j1 = intersections[x][1]
        l3[i1][j1][0] = -4
        check5(i1,j1)
l3_2 = copy.deepcopy(l3)
for i1 in range(len(l3_2)):
    for j1 in range(len(l3_2[i1])):
        if l3_2[i1][j1][0] == 2:
            path += 1
            check6(i1,j1)
for i1 in range(len(l3_3)):
    for j1 in range(len(l3_3[i1])):
        if l3_3[i1][j1][0] >= 0:
            areas += 1
            check7(i1,j1)
horizon.sort()
vertical.sort()
for x in range(len(horizon)):
    for i in range(len(horizon)):
        if [horizon[i][0],horizon[i][2],horizon[i][2]+1] in horizon:
            horizon[horizon.index([horizon[i][0],horizon[i][2],horizon[i][2]+1])]=[-1,-1,-1]
            horizon[i]=[horizon[i][0],horizon[i][1],horizon[i][2]+1]
            
            break
#print(horizon)
for x in range(len(vertical)):
    for i in range(len(vertical)):
        if [vertical[i][0],vertical[i][2],vertical[i][2]+1] in vertical:
            vertical[vertical.index([vertical[i][0],vertical[i][2],vertical[i][2]+1])]=[-1,-1,-1]
            vertical[i]=[vertical[i][0],vertical[i][1],vertical[i][2]+1]
            
            break
horizon.sort()
vertical.sort()
for i in range(len(l3)):
    for j in range(len(l3[i])):
        if l3[i][j][0] == 2:
            
            if ('r' in l3[i][j]) :
                dash_h.append([i,j,j+1])
                if j+1<= len(l3[i])-1:
                    l3[i][j+1][3] = None
            if ('l' in l3[i][j]) :
                
                dash_h.append([i,j-1,j])
                if j-1 >= 0:
                    l3[i][j-1][4] = None
            if ('d' in l3[i][j]) :
                dash_v.append([j,i,i+1])
                if i+1 <= len(l3)-1:
                    l3[i+1][j][1] = None
            if ('u' in l3[i][j]) :
                dash_v.append([j,i-1,i])
                if i-1 >= 0:
                    l3[i-1][j][2] = None
dash_h.sort()
dash_v.sort()
for x in range(len(dash_h)):
    for i in range(len(dash_h)):
        if [dash_h[i][0],dash_h[i][2],dash_h[i][2]+1] in dash_h:
            dash_h[dash_h.index([dash_h[i][0],dash_h[i][2],dash_h[i][2]+1])]=[-1,-1,-1]
            dash_h[i]=[dash_h[i][0],dash_h[i][1],dash_h[i][2]+1]
            
            break
for x in range(len(dash_v)):
    for i in range(len(dash_v)):
        if [dash_v[i][0],dash_v[i][2],dash_v[i][2]+1] in dash_v:
            dash_v[dash_v.index([dash_v[i][0],dash_v[i][2],dash_v[i][2]+1])]=[-1,-1,-1]
            dash_v[i]=[dash_v[i][0],dash_v[i][1],dash_v[i][2]+1]
            
            break
dash_h.sort()
dash_v.sort()
##print(dash_h)
##print(dash_v)
##for x in range(len(dash)):
##    for i in range(len(dash)):
##        if [dash[i][1],dash[i][1]+1] in dash:
##            dash_h.append([dash[i][0],dash[i][1],dash[i][1]+1])
##        if [dash[i][0],dash[i][0]+1] in dash:
##            dash_v.append([dash[i][1],dash[i][0],dash[i][0]+1])
areas = areas - len(inaccessible)
file = file.split('.')
printer = args.printer
if printer:
    date1 = '\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes.misc}\n\\usepackage[margin=0cm]{geometry}\n\pagestyle{empty}\n\\tikzstyle{every node}=[cross out, draw, red]\n\n\\begin{document}\n\n\\vspace*{\\fill}\n\\begin{center}\n\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n% Walls\n'
    date2 = '\end{tikzpicture}\n\end{center}\n\\vspace*{\\fill}\n\n\end{document}\n'
    if not os.path.exists(file[0]+'.tex'):
        f = open(str(file[0])+'.tex', 'a')
        f.write(date1)
        f_write()
        f.write(date2)
        f.close()
    else:
        f = open(str(file[0])+'.tex', 'w')
        f.write(date1)
        f_write()
        f.write(date2)
        f.close()
if not printer:
    
    if gate == 0:
        print('The maze has no gate.')
    elif gate == 1:
        print('The maze has a single gate.')
    else:
        print('The maze has {} gates.'.format(gate))
    if wall == 0:
        print('The maze has no wall.')
    elif wall == 1:
        print('The maze has a single wall that are all connected.')
    else:
        print('The maze has {} sets of walls that are all connected.'.format(wall))
    if len(inner) == 0:
        print('The maze has no inaccessible inner point.')
    elif len(inner) == 1:
        print('The maze has a unique inaccessible inner point.')
    else:
        print('The maze has {} inaccessible inner points.'.format(len(inner)))
    if areas == 0:
        print('The maze has no accessible area.')
    elif areas == 1:
        print('The maze has a unique accessible area.')
    else:
        print('The maze has {} accessible areas.'.format(areas))
    if set_cul ==0:
        print('The maze has no accessible cul-de-sac.')
    elif set_cul == 1:
        print('The maze has accessible cul-de-sacs that are all connected.')
    else:
        print('The maze has {} sets of accessible cul-de-sacs that are all connected.'.format(set_cul))                   
    if path == 0:
        print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
    elif path == 1:
        print('The maze has a unique entry-exit path with no intersection not to cul-de-sac.')
    else:
        print('The maze has {} entry-exit paths with no intersections not to cul-de-sacs.'.format(path))      
                    
                    

        
        
        
            
    
