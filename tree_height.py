# python3

import sys
import threading
import numpy as np
import os

def compute_height(n, parents):
    tree_height=np.zeros(n,dtype=int)
    for i in range(n):
        checker=i
        height=0
        while checker!=-1:
            if tree_height[checker]!=0:
                height+=tree_height[checker]
                break
            height+=1
            checker=parents[checker]
        tree_height[i]=height
    return np.max(tree_height)


def main():
    # implement input form keyboard and from files
    input_IF=input()
    if input_IF[0]=="I":
        # input number of elements
        n=int(input())
        # input values in one variable, separate with space, split these values in an array
        parents=list(map(int,input().split()))
         # call the function and output it's result  
        print(compute_height(n, parents))
    elif input_IF[0]=="F":
        tests=input()
        if "a" not in tests:
            # let user input file name to use, don't allow file names with letter a
            with open("test/"+tests) as f:
                # input number of elements
                n=int(f.readline())
                # input values in one variable, separate with space, split these values in an array
                parents=list(map(int, f.readline().split()))
                # call the function and output it's result  
                print(compute_height(n,parents))
    # account for github input inprecision   
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
