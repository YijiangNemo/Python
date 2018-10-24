##Written by Yijiang Wu
##use Truth table to exclude the wrong solution and use 'key word' to
##modify the Truth table and find the sir name

import os
import os.path
import sys
filename = input('Which text file do you want to use for the puzzle? ')
if os.path.exists(filename) == False:
    print('Error:there is no file with that name')
    sys.exit()


f = open(filename,'r')
l = []
ll = []
name = []
sentence = []
speaker = []
table = []
## use the key word to modify the truth table
def check(table):
##A or B is XX = at least one of A B is XX
    if 'or' in sentence:
        sentence[sentence.index('or')] = 'least'

## 'I am a Knave' is a contradiction .so it must be no solution
    if ['I', 'am', 'a', 'Knave'] == sentence:
        table = []
        return []
    for x in range(len(sentence)):
        sentence_name = []
        for i1 in range(len(sentence)):
            if sentence[i1] in name:
                sentence_name.append(sentence[i1])
## if at least one of A B C is Knave/Knight ,if speaker is Knight situation:
## both A B C are Knight/Knave must be wrong,if speaker is Knave,Situation:
## at least one of A B C is Knave/Knight must be wrong
        if sentence[x] == 'least':
            if 'Knave' in sentence or 'Knaves' in sentence:
                for i in range(len(sentence)):
                    if sentence[i] in name:
##                        sentence_name = []
##                        for i1 in range(len(sentence)):
##                            if sentence[i1] in name:
##                                sentence_name.append(sentence[i1])
                        for i1 in range(len(table)):
                            match = True
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] != 1:
                                    match = False
                            if match == True:
                                table[i1] = ['n']*len(name)

                    if sentence[i] == 'I':
                        for i1 in range(len(table)):
                            if table[i1][name.index(speaker[0])] == 0:
                                table[i1] = ['n']*len(name)
                    if ('us' in sentence) and ('I' not in sentence):
                        match = [1]*len(name)
                        for i1 in range(len(table)):
                            if table[i1] == match:
                                table[i1] = ['n']*len(name)
                    
            if 'Knight' in sentence or 'Knights' in sentence:
                if 'I' in sentence:                   
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 0:
                            match = False
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    match = True
                            if match == True:
                                table[i1] = ['n']*len(name)
                elif 'us' not in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            match = True
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    match = False
                            if match == True:
                                table[i1] = ['n']*len(name)
                        else:
                            match = False
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    match = True
                            if match == True:
                                table[i1] = ['n']*len(name)
                if ('us' in sentence) and ('I' not in sentence):
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 0:
                            match = False
                            for i2 in range(len(name)):
                                if table[i1][i2] == 1:
                                    match = True
                            if match == True:
                                table[i1] = ['n']*len(name)
##                    if sentence[i] in name:
##                        for i1 in range(len(table)):
##                            if table[i1][name.index(sentence[i])] != 0:
##                                table[i1] = ['n']*len(name)
##                    if sentence[i] == 'I':
##                        for i1 in range(len(table)):
##                            if table[i1][name.index(speaker[0])] != 0:
##                                table[i1] = ['n']*len(name)

## if at most one of A B C is Knight/Knave,if the speaker is knight,situation:more than one
## Knight/Knave in A B C must be wrong,if the speaker is Knave,situation: less
## than one of Knight/Knave must be wrong
        if sentence[x] == 'most':
            if 'Knave' in sentence or 'Knaves' in sentence:              
                if 'I' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count > 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count < 1:
                                table[i1] = ['n']*len(name)
                elif 'us' not in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count > 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count <= 1:
                                table[i1] = ['n']*len(name)
                if ('us' in sentence) and ('I' not in sentence):
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 0:
                                    count += 1
                            if count > 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 0:
                                    count += 1
                            if count <= 1:
                                table[i1] = ['n']*len(name)
##                match = [1]*len(table[0])
##                match[name.index(speaker[0])] = 0
##                for i in range(len(table)):
##                    if table[i] == match:
##                        table[i] = ['n']*len(name)
##                    if table[i][name.index(speaker[0])] == 1:
##                        count = 0
##                        for x in table[i]:
##                            if x == 0:
##                                count += 1
##                        if count > 1:
##                            table[i] = ['n']*len(name)
            if 'Knight' in sentence or 'Knights' in sentence:
                if 'I' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            match = False
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    match = True
                            if match == True:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count <= 1:
                                table[i1] = ['n']*len(name)
                elif 'us' not in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count > 1:
                                table[i1] = ['n']*len(name)
                    else:
                        count = 0
                        for i2 in range(len(sentence_name)):
                            if table[i1][name.index(sentence_name[i2])] == 1:
                                count += 1
                        if count <= 1:
                            table[i1] = ['n']*len(name)
                if ('us' in sentence) and ('I' not in sentence):
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 1:
                                    count += 1
                            if count != 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 1:
                                    count += 1
                            if count <= 1:
                                table[i1] = ['n']*len(name)
                    
##if exactly one of A B C is knight/Knave,count the number of Knight/Knave and
##check if the number is equal to 1
        if sentence[x] == 'exactly' or sentence[x] == 'Exactly':
            if 'Knave' in sentence or 'Knaves' in sentence:
                if 'I' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count != 0:
                                table[i1] = ['n']*len(name)
                        else:
                            match = True
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    match = False
                            if match == True:
                                table[i1] = ['n']*len(name)
                elif 'us' not in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count != 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 0:
                                    count += 1
                            if count == 1:
                                table[i1] = ['n']*len(name)
                if ('us' in sentence) and ('I' not in sentence):
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 0:
                                    count += 1
                            if count != 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 0:
                                    count += 1
                            if count == 1:
                                table[i1] = ['n']*len(name)
            if 'Knight' in sentence or 'Knights' in sentence:
                if 'I' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count != 0:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count == 1:
                                table[i1] = ['n']*len(name)
                elif 'us' not in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count != 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(sentence_name)):
                                if table[i1][name.index(sentence_name[i2])] == 1:
                                    count += 1
                            if count == 1:
                                table[i1] = ['n']*len(name)
                if ('us' in sentence) and ('I' not in sentence):
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 1:
                                    count += 1
                            if count != 1:
                                table[i1] = ['n']*len(name)
                        else:
                            count = 0
                            for i2 in range(len(table[0])):
                                if table[i1][i2] == 1:
                                    count += 1
                            if count == 1:
                                table[i1] = ['n']*len(name)
### if all of A B C are Knight/Knave,if speaker is Knight,situation:more than one
### of A B C is Knave/Knight must be Wrong,if speaker is Knave,situation:
### all of A B C are Knight/Knave must be wrong
        if sentence[x] == 'all' or sentence[x] == 'All':
            if 'Knave' in sentence or 'Knaves' in sentence:
                for i1 in range(len(table)):
                    if table[i1][name.index(speaker[0])] == 1:
                        table[i1] = ['n']*len(name)
                    else:
                        match = [0]*len(name)
                        if table[i1] == match:
                            table[i1] = ['n']*len(name)
            if 'Knight' in sentence or 'Knights' in sentence:
                for i1 in range(len(table)):
                    if table[i1][name.index(speaker[0])] == 1:
                        match = [1]*len(name)
                        if table[i1] != match:
                            table[i1] = ['n']*len(name)
        if 'least' not in sentence and'most' not in sentence and'exactly' not in sentence and'Exactly' not in sentence and'all' not in sentence and'All' not in sentence:
            if 'are' in sentence:
                if 'Knave' in sentence or 'Knaves' in sentence:
                    if 'I' in sentence:
                        for i1 in range(len(table)):
                            if table[i1][name.index(speaker[0])] == 1:

                                table[i1] = ['n']*len(name)
                            else:
                                count = 0
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 1:
                                        count += 1
                                if count == 0:
                                    table[i1] = ['n']*len(name)
                    else:
                        for i1 in range(len(table)):
                            if table[i1][name.index(speaker[0])] == 1:
                                match = False
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 1:
                                        match = True
                                if match == True:
                                    table[i1] = ['n']*len(name)
                            else:
                                count = 0
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 1:
                                        count += 1
                                if count == 0:
                                    table[i1] = ['n']*len(name)
                if 'Knight' in sentence or 'Knights' in sentence:
                    if 'I' in sentence:
                        for i1 in range(len(table)):
                            if table[i1][name.index(speaker[0])] == 1:
                                count = 0
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 0:
                                        count += 1
                                if count != 0:
                                    table[i1] = ['n']*len(name)
                    else:
                        for i1 in range(len(table)):
                            if table[i1][name.index(speaker[0])] == 1:
                                count = 0
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 0:
                                        count += 1
                                if count != 0:
                                    table[i1] = ['n']*len(name)
                            else:
                                count = 0
                                for i2 in range(len(sentence_name)):
                                    if table[i1][name.index(sentence_name[i2])] == 0:
                                        count += 1
                                if count == 0:
                                    table[i1] = ['n']*len(name)
                
            if 'is' in sentence:
##                print('is')
                if 'Knave' in sentence or 'Knaves' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            if table[i1][name.index(sentence_name[0])] == 1:
                                table[i1] = ['n']*len(name)
                        else:
                            if table[i1][name.index(sentence_name[0])] == 0:
                                table[i1] = ['n']*len(name)
                if 'Knight' in sentence or 'Knights' in sentence:
                    for i1 in range(len(table)):
                        if table[i1][name.index(speaker[0])] == 1:
                            if table[i1][name.index(sentence_name[0])] == 0:
                                table[i1] = ['n']*len(name)
                        else:
                            if table[i1][name.index(sentence_name[0])] == 1:
                                table[i1] = ['n']*len(name)
    return table
                                
                    
## split the txt file      
for line in f:
    int_line = []
    for c in line.split():
        for a in c.split(','):
            if a != '':
                for b in a.split('.'):
                    for d in b.split('!'):
                            for k in d.split('?'):
                                if k == '':
                                    int_line.append('.')
                                else:
                                    for k1 in k.split(':'):
                                        if k1 != '' :
                                            for e in k1.split('"'):
                                                int_line.append(e)
                                        else:
                                            int_line.append(':')
           
                                
    l.append(int_line)
for i in range (len(l)):
    for j in range(len(l[i])):
        ll.append(l[i][j])
## use the key word 'Sirs' and 'Sir' to find the name
for i in range(len(ll)):
    ##Sirs means more than 2 name ,use 'and' to find the last name and break
    if ll[i] == 'Sirs':
        for j1 in range(i+1,len(ll)):
            if ll[j1] == 'and':
                name.append(ll[j1+1])
                break
            if ll[j1] != '':
                name.append(ll[j1])
    if ll[i]  == 'Sir' :
        name.append(ll[i+1])
name = list(set(name))            
name.sort()
## create the Truth table
table = [[] for i in range(2**len(name))]
for i in range(len(table)):
    for j in range(len(name)):
        table[i].append(1)
for j in range(len(name)):
    gap = len(table)//2**(j+1)
    i = 0
    while i <= len(table):
        for x in range(gap):
            if i+x < len(table):
                table[i+x][j] = 0
        
        i += 2*gap
## find the speaker name and the word he say by using '' as a signal that he
## begin to speak
for i in range(len(ll)):
    if ll[i] == '':
##        if ll[i-1] == ':':
        for i2 in range(i,-1,-1):
            if ll[i2] in name:
                speaker.append(ll[i2])
                break
            if ll[i2] == '.':
                break
        
        for i1 in range(i+1,len(ll)):
            
            sentence.append(ll[i1])
            if ll[i1+1] == '':
                ll[i1+1] = '.'
                ll[i1+2] = '.'
                if len(speaker) < 1:
                    for i2 in range(i1+2,len(ll)):
                        if ll[i2] in name:
                            speaker.append(ll[i2])
                            break
                table = check(table)
                sentence = []
                speaker = []
                break
## the wrong situation is ['n']*len(name),exclude that,we will find the solution
solution = 0
for i in range(len(table)):
    if table[i] != ['n']*len(name):
        solution += 1

if solution == 1:
    sol = []
    for i in range(len(table)):
        if table[i] != ['n']*len(name):
            sol = table[i]
##print the output
print('The Sirs are:',end = ' ')
for i in range(len(name)):
    print(name[i],end=' ')
print()
if solution == 0:
    print('There is no solution.')
elif solution == 1:
    print('There is a unique solution:')
    for i in range(len(sol)):
        if sol[i] == 0:
            print('Sir '+name[i]+' is a Knave.')
        else:
            print('Sir '+name[i]+' is a Knight.')
else:
    print('There are {} solutions.'.format(solution))
    
