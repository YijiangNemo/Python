##file = input('Which data file do you want to use?')
import os
import os.path
import sys
file = input('Which data file do you want to use?')
if os.path.exists(file) == False:
    print('Error:there is no such file')
    sys.exit()
l = []


f= open(file,'r')
for line in f:
    int_line = []
    for digit in line.split():
        int_line.append(int(digit))
    l.append(int_line)
def refresh(s,s0,s1,s2,n):
    #print('begin',s,s0,s1)
    n = []
    f= open(file,'r')
    for line in f:
        int_line = []
        for digit in line.split():
            
            int_line.append(int(digit))
        n.append(int_line)
    ##print(n)
    if s1 ==0:
        return find(s,s0,s1,s2,n)
    else:
        return rule(s,s0,s1,s2,n)

def find(s,s0,s1,s2,n):
    s2 = 0
    #print('find')
    for i1 in range (len(l)):
        s2 = s2 + l[i1][1]
        s = s2 // len(l)
    
    s1 = s
    s = s//2
    #print(s,s0,s1)
    return rule(s,s0,s1,s2,n)
    
def loop():
    m = []
    for i in range (len(l)-1):
        if l[i][0] > l[i+1][0]:
            m = l[i+1]
            l[i+1] = l[i]
            l[i] = m
            return loop()

    return l



def rule(s,s0,s1,s2,n):
    #print('rule')
    #print(s,s0,s1)
    
    for i3 in range(len(n)-1):
        if n[i3][1] < s:
            n[i3+1][1] = n[i3+1][1] + (n[i3][1]-s-(n[i3+1][0]-n[i3][0]))
            
            
        if n[i3][1] > s:
            if n[i3][1]-n[i3+1][0]+n[i3][0]-s>0:
                n[i3+1][1] = n[i3+1][1] + (n[i3][1]-s-(n[i3+1][0]-n[i3][0]))
                
            
            
                
    #print(n)
    if n[len(n)-1][1] > s:
        
        
        return judge1(s,s0,s1,s2,n)
    if n[len(n)-1][1] < s:
        
        return judge2(s,s0,s1,s2,n)
    if n[len(n)-1][1] == s:
        print('The maximum quantity of fish that each town can have is',s)

def judge1(s,s0,s1,s2,n):
    ##print('1')
    ##print(s,s0,s1)
    if s1 - s0 <= 1:
        #print('yes')
        print('The maximum quantity of fish that each town can have is',s0)
        #print(n)
    else:
        #print('no1')
        s0 = s
        s = round((s0 + s1)//2)
        return refresh(s,s0,s1,s2,n)
        
##        if (s0 + s1) % 2 == 0:
##            s0 = s
##            s = (s0 + s1)//2
##            print(s,s0,s1)
##            return refresh(s,s0,s1,s2,n)
##            
##        else:
##            s0 = s
##            s = (s0 + s1)//2 +1
##            print(s,s0,s1)
##            return refresh(s,s0,s1,s2,n)
    
def judge2(s,s0,s1,s2,n):
    ##print('2')
    ##print(s,s0,s1)
    if s1 - s0 <= 1:
        #print('yes')
        print('The maximum quantity of fish that each town can have is',s0)
        #print(n)
    else:
        #print('no2')
        s1 = s
        s = round((s0 + s1)/2)
        return refresh(s,s0,s1,s2,n)
##        if (s0 + s1) % 2==0:
##            s1 = s
##            s = (s0 + s1)//2
##            
##            print(s,s0,s1)
##            return refresh(s,s0,s1,s2,n)
##        else:
##            s1 = s
##            s = (s0 + s1)//2 +1
##            
##            print(s,s0,s1)
##            return refresh(s,s0,s1,s2,n)


if __name__ == '__main__':
    n = []
    s = 0
    s0 = 0
    s1 = 0
    s2 = 0
    loop()
    refresh(s,s0,s1,s2,n)
    
       
    
    
