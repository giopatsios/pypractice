# %%
#   Given an array of integers and a positive integer k, determine the number of pairs (i,j), where i<j and ar[i]+ar[j] is divisible by k.
import numpy as np

ar = [1,25,0,30,43]         # that's a 'random' arraw of numbers
ar.sort()               # which I am sorting in order: smallest to largest
k = 5       # and that's a random integer

def occurence_counter(ar):
    noumero = []                        # an empty array
    for i in range(len(ar)):            # two indeces running this if
        for j in range(len(ar)):
            if (i < j) & ( (ar[i]+ar[j]) % k == 0 ): 
                noumero += '1'          # add a '1' when demands are met, otherwise adds '0'
            else:
                noumero += '0'
    return noumero.count('1')           # count 1s in the end, to find how many times it happened

occurence_counter(ar)               # returns the number conditions were met



