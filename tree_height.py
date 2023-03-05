# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    roots = {}
    for i in range(n):
        if parents==-1:
            tree=i
        else:
            if parents[i] in roots:
                parents[i].append(i)
            else:
                parents[i]=i
    # Your code here
    def find_height(oneroot):
        if oneroot in roots:
            max_height = 0
            for i in roots[oneroot]:
                height=height(i)
                if height>max_height:
                    max_height=height
            return max_height
        else:
            return 0
    return max_height


def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    n = int(input())
    # input values in one variable, separate with space, split these values in an array
    parents = list(map(input().split()))
    # call the function and output it's result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
