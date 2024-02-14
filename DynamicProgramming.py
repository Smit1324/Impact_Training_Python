# A program can be solved using:
# Iterative Method
# Recurssive Method
# Tabular Method

# Using Tabular and memorization comes under the dynamic programming
# The first 2 approaches will take more time and more memory i.e., Time complexity is more.
# Optimization can be achieved through dynamic programming i.e., Memory and Time Optimizations

# Dynamic Programming will take more time as compared to the iterative method but it will take less time as compared to the recursive method.

# Using Iterative Method: 
# Implementation of fibinacci series using iterative method
# Time Complexity: O(n)
# Space Complexity: O(1)
# n=int(input("Enter the number: "))
# a=0
# b=1
# print(a,b,end=" ")
# c=a+b
# while(c<=n):
#     print(c,end=" ")
#     a=b
#     b=c
#     c=a+b

# Write a program to find nth term in the fibonacci series using iterative method.
# def fib(n):
#     a=0
#     b=1
#     if n<0:
#         print("Invalid terms")
#     elif n==0:
#         return a
#     elif n==1:
#         return b
#     else:
#         for i in range(2,n+1):
#             c=a+b
#             a=b
#             b=c
#     return b
# print(fib(5))

# Write a program to find nth term in the fibonacci series using recursive method.
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(6))

# Write a program to find nth term in the fibonacci series using tabular method.
# In this approach, we are going t store the result in the mempry and we are going to calculate the value only once. If next time, same value is required then we are going to use the value from the memory.
# So, by this approach we are going to save the time and memory.
# def fib(n):
#     f=[0,1]
#     for p in range(2,n+1):
#         f.append(f[p-1]+f[p-2])
#     return f[n]
# print(fib(6))

# Write a program to find sum of left leaf nodes in the binary tree.
# class Node:
#     def __init__(self,key):
#         self.left=None
#         self.right=None
#         self.val=key
# def sumOfLeftLeaf(root):
#     if root is None:
#         return 0
#     if root.left is not None and root.left.left is None and root.left.right is None:
#         return root.left.val+sumOfLeftLeaf(root.right)
#     return sumOfLeftLeaf(root.left)+sumOfLeftLeaf(root.right)
# root=Node(20)
# root.left=Node(9)
# root.right=Node(49)
# root.right.left=Node(23)
# root.right.right=Node(52)
# root.right.right.left=Node(50)
# root.left.left=Node(5)
# root.left.right=Node(12)
# root.left.right.right=Node(12)
# print(sumOfLeftLeaf(root))