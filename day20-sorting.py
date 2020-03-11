#!/bin/python3

import sys


def mergeSort(arr):
    count=0
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                count+=1
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return [arr ,count]
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
ans=mergeSort(a)
print("Array is sorted in {} swaps.".format(ans[1]))
print('First Element: {}'.format(ans[0][0]))
print('Last Element: {}'.format(ans[0][-1]))
