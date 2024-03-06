# KNAP-SACK PROBLEM using Dynamic Programming

# Problem Statement:
# The knap sack problem is an example of a combinatorial optimization problem, which seeks to maximize the benefit of objects in a knapsack without exceeding its capacity. The problem can be solved using dynamic programming.
# It is also known as root sack problem.
# The name of the problem is defined as Given a bag with maximum bag weight capacity of W, and set of items, each having a weight and a value associated with it.
# Decide the number of each item to take in a collection such that the total weight is less than or equal to W and the total value is as large as possible.

# Types of knap sack problem:
# 1. 0/1 knap sack problem
# 2. Fractional knap sack problem
# 3. Bounded knap sack problem
# 4. Unbounded knap sack problem

# We are given few items, where each item has some weight(wi) and value(vi), we are also given a bag of capacity W. The target is to put the items into the bag, such that the sum of values associated with that is maximum possible.
# Note that, we can either out an item completely into the bag or cannot put it at all.


def knapsack(wt, val, W, n):

    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n-1] <= W:
        t[n][W]=max(val[n-1]+knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W]=knapsack(wt, val, W, n-1)
        return t[n][W]

# Driver code
if __name__=='__main__':
    profit=[1,2,3]
    weight=[4,5,1]
    W=4
    n=len(profit)
    t=[[-1 for i in range(W+1)] for j in range(n+1)]
    print(t)
    print(knapsack(weight, profit, W, n)) # 220