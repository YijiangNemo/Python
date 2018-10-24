# Prompts the user for two nonnegative integers, generates a list L of random numbers
# between 0 and 19, of length the second input, outputs L, and outputs L again where
# all elements have been rearranged so that L is now of the form L_1 L_2 ... L_k and:
# - * L_1 starts with the first element of L,
#   * L_2 starts with the first element of L with all elements of L_1 removed,
#   ...
#   * L_k starts with the first element of L with all elements of L_1, ..., L_{k-1} removed;
# - * L_1 is a stricly increasing subsequence of L of longest possible length,
#   * L_1 is a stricly increasing subsequences of L with all elements of L_1 removed
#     of longest possible length,
#   ...
#   * L_k is a stricly increasing subsequences of L with all elements of L_1, ..., L_{k-1} removed
#     of longest possible length.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint


max_value = 19

try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('The generated list is:')
print('  ', L)

# REPLACE THIS COMMENT WITH YOUR CODE
LL = []
for _ in range(length):
    cnumber = -2
    
    for i in L:
        if i > cnumber and i > -1:
            LL.append(i)
            cnumber = i
            L[L.index(i)] = -1

L = LL
print('The transformed list is:')
print('  ', L)
