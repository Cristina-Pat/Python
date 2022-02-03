
#calculate Fibonacci numbers for a given n
from turtle import left
from typing import Callable


def F(n):
    if n == 0 or n == 1: #exit condition or break case
        return n
    else:
        return F(n-1) + F(n-2)
    

#calculate the factorial of a number
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1) #divide

#merge two lists into one with kesy in non-decreasing way
def merge(leftList: list, rightList:list, key: Callable) -> list:
    leftIndex = 0
    rightIndex = 0
    sorted = []
    while leftIndex < len(leftList) and rightIndex < len(rightList):
        leftItem = leftList[leftIndex]
        rightItme = rightList[rightIndex]
        if key(leftItem) <= key(rightItme):
            sorted.append(leftItem)
            leftIndex += 1
        else:
            sorted.append(rightItme)
            rightIndex += 1
    for index in range (leftIndex, len(leftList)):
        sorted.append(leftList[index])
    for index in range (rightIndex, len(rightList)):
        sorted.append(rightList[index]) 
    return sorted

#return a permutation with keys in non-decreasing order
def mergeSort(unsorted: list, key: Callable) -> list:
    n = len(unsorted)
    if n < 2:
        return unsorted
    middle = n//2
    left = mergeSort(unsorted[0:middle], key)
    right = mergeSort(unsorted[middle:n], key)
    return merge(left, right, key)
    

print(factorial(3))
print(F(3))