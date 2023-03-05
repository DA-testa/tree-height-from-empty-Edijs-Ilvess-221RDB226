# python3

import sys
import threading
import numpy
import os

def compute_height(n, parents):
    # Write this function
    roots = {}
    for i in range(n):
        if parents[i]==-1:
            tree=i
        else:
            if parents[i] in roots:
                roots[parents[i]].append(i)
            else:
                roots[parents[i]]=[i]
    # Your code here
    def find_height(oneroot):
        if oneroot in roots:
            max_height = 0
            for i in roots[oneroot]:
                if i!=oneroot:
                   height=find_height(i)
                   if height>max_height:
                        max_height=height
            return 1+max_height
        else:
            return 1
    max_height = 0
    for i in roots:
        height=find_height(i)
        if height>max_height:
            max_height=height
    return max_height


def main():
    # implement input form keyboard and from files
    input_IF=input()
    if input_IF[0]=="I":
        n=int(input())
        parents=list(map(int,input().split()))
        print(compute_height(n, parents))
    elif input_IF[0]=="F":
        tests=input()
        if "a" not in tests:
            with open("test/"+tests) as f:
                n=int(f.readline())
                parents=list(map(int, f.readline().split()))
                print(compute_height(n,parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result     
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
