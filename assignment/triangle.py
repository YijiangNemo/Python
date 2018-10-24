import os
import os.path
import sys
file = input('Which data file do you want to use?')
if os.path.exists(file) == False:
    print('Error:there is no such file')
    sys.exit()




l=[]
m = []
n = 0
i3 = 0
f= open(file,'r')
for line in f:
    int_line = []
    for digit in line.split():
        int_line.append(int(digit))
    l.append(int_line)
for k in range(len(l)):
    for kk in range(k+1):
        l[k][kk] = [l[k][kk],1]
for i in range(len(l)-1,-1,-1):
    ##print(i)
    for j in range(len(l[i])-1):
        ##print('j=',j)
        if l[i][j][0] > l[i][j+1][0]:
            
            l[i-1][j][0] = l[i-1][j][0] +l[i][j][0]
            l[i-1][j][1] = l[i][j][1]
                
        if l[i][j][0] == l[i][j+1][0]:
            l[i-1][j][0] = l[i-1][j][0] +l[i][j][0]
            l[i-1][j][1] = l[i][j][1] +l[i][j+1][1]
            
            ##m.append((l[l[i-1][j],))
            ##print('y',l[i-1][j])
        if l[i][j][0] < l[i][j+1][0]:
            l[i-1][j][0] = l[i-1][j][0] + l[i][j+1][0]
            l[i-1][j][1] = l[i][j+1][1]
            ##n.append(j+1)
            ##print('n',l[i-1][j])

print('The largest sum is:',l[0][0][0])

j1 = 1
for i1 in range(1,len(l)):
    if l[i1][j1-1][0] >= l[i1][j1][0]:
        
        m.append(l[i1-1][j1-1][0]-l[i1][j1-1][0])
        
    else:
        m.append(l[i1-1][j1-1][0]-l[i1][j1][0])
        
        j1 += 1
    
if l[len(l)-1][j1-1][0] >= l[len(l)-1][j1][0]:
    ##print('j1=',j1)
    m.append(l[len(l)-1][j1-1][0])
else:
    m.append(l[len(l)-1][j1][0])

print('The number of paths yielding this sum is:',l[0][0][1])                                            
print('The leftmost path yielding this sum is:',m)                                       


##for i2 in range(1,len(l)):
##    for j2 in range(i2):
##        if (l[i2][j2] == l[i2][j2+1])and(l[i2][j2] == max(l[i2])):
##            ##print('i2',i2)
##            n = 2**i2
##            i3 = i2
##        else:
##            break
##            
##            
##o = []
##o = l[i3+1]
##for j3 in range(i3+2):
##    ##print(i3+1)
##    if (l[i3+1][j3] == max(o))and(i3+1 != len(l)-1):
##        n += 1
##
##n = 0
##o = []
##for ii in range(1,len(l)):
##    if l[ii][n]<=l[ii][n+1]:
##        o.append(1)
##        if l[ii][n]==l[ii][n+1]:
##            o.append(ii)
##            for jj in range(ii+1,len(l)):
##                if l[jj][n]<=l[jj][n+1]:
##                    o.append(1)
##                    if l[jj][n] == l[jj][n+1]:
##                        o.append(1)
##                else:
##                    o.append(1)
##        n += 1
##    else:
##        o.append(1)
####
##o = []
##def look():
##    path = 1
##    for ii in range(1,len(l)):
##        for jj in range(ii):
##            if l[ii][jj] == l[ii][jj+1]:
##                print('ee',ii,jj)
##                find(ii,jj,l,path)
##                
##                find2(ii,jj,l,path)
##                raise
            
            
            
            
        
##def find(ii,jj,l,path):
##    print('find')
##    print(ii,jj)
##    
##    for i0 in range(ii+1,len(l)):
##        for j0 in range(i0-1):
##            if l[i0][j0+jj] == l[i0][j0+jj+1]:
##                path += 1
##                print('1',path)
##                return find(i0,j0,l,path)
##    
##    o.append(path)
##    
##    
##def find2(ii,jj,l,path):
##    print('find2',path)
##    print(ii,jj)
##    
##    for ii0 in range(ii+1,len(l)):
##        for jj0 in range(ii0-1):
##            if l[ii0][jj0+jj+1] == l[ii0][jj0+jj+2]:
##                path += 1
##                print('2',path)
##                return find2(ii0,jj0,l,path)
##    o.append(path)
    
 
        
                    
                                         
