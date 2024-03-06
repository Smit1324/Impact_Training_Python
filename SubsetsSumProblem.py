# def isSubsetSum(arr, n, sum):
#     if sum == 0:
#         return True
#     if n == 0 and sum != 0:
#         return False
#     if arr[n-1] > sum:
#         return isSubsetSum(arr, n-1, sum)
#     return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

# arr = [3, 34, 4, 12, 5, 2]
# sum = 9
# n = len(arr)
# if isSubsetSum(arr, n, sum) == True:
#     print("Found a subset with given sum")
# else:
#     print("No subset with given sum")


# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum


# def isSubsetSum(set, n, sum):

# 	subset = ([[False for i in range(sum + 1)]
# 			for i in range(n + 1)])

# 	for i in range(n + 1):
# 		subset[i][0] = True

# 	for i in range(1, sum + 1):
# 		subset[0][i] = False

# 	for i in range(1, n + 1):
# 		for j in range(1, sum + 1):
# 			if j < set[i-1]:
# 				subset[i][j] = subset[i-1][j]
# 			if j >= set[i-1]:
# 				subset[i][j] = (subset[i-1][j] or
# 								subset[i - 1][j-set[i-1]])

# 	return subset[n][sum]


# if _name_ == '_main_':
# 	set = [3, 34, 4, 12, 5, 2]
# 	sum = 9
# 	n = len(set)
# 	if (isSubsetSum(set, n, sum) == True):
# 		print("Found a subset with given sum")
# 	else:
# 		print("No subset with given sum")


# LONGEST POSSIBLE SUB SEQUENCE

# Given an array of size n, the task is to find the length of longest increasing subsequence i.e., the longest subsequence such that all elements of the subsequence are sorted in ascending order.

# global maximum
# def _lis(arr, n):
#     global maximum
#     if n == 1:
#         return 1
#     maxEndingHere = 1
#     for i in range(1, n):
#         res = _lis(arr, i)
#         if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
#             maxEndingHere = res+1
#     maximum = max(maximum, maxEndingHere)
#     return maxEndingHere

# def lis(arr):
#     global maximum
#     n = len(arr)
#     maximum = 1
#     _lis(arr, n)
#     return maximum

# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# print("Length of lis is", lis(arr))

# Dynamic Programming implementation of LIS problem

# def lis(arr):
#     n = len(arr)
#     lis = [1]*n
#     for i in range(1, n):
#         for j in range(0, i):
#             if arr[i] > arr[j] and lis[i] < lis[j] + 1:
#                 lis[i] = lis[j]+1
#     maximum = 0
#     for i in range(n):
#         maximum = max(maximum, lis[i])
#     return maximum

# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# print("Length of lis is", lis(arr))


# HASH MAP, HASH SET, HASH TABLE & HASH FUNCTION

# Hash Set is a collection of objects.

# In Hash Table, data was stored in the form of key & value pair.
# Hash Set internally uses Hash Table to store the elements.
# Just like the Set, Hash Set also don't allow duplicate elements.

# Hash Map & Hash Table are the same things i.e., the way of storing and organising information.
# Hash Map and Hash Table are implemented by dictionary in python.
# Hash Map are in key and value pair.

# Hash Function is a function that accepts a string and returns a number.
# Hashing is a technique used in computer science to store and retrieve data efficiently.
# It involves converting data into pixel sixed values called hash codes.
# This hash codes are used as indexes through store the data in data structure like hash maps, hash tables, hash sets etc.

# hash_set=set()
# print(type(hash_set))
# hash_set.add(1)
# hash_set.add(2)
# hash_set.add(3)
# hash_set.add(4)
# hash_set.add(5)
# print(hash_set)
# search_ele=2
# if search_ele in hash_set:
#     print(f"{search_ele} is present in the hash set")
# else:
#     print(f"{search_ele} is not present in the hash set")

# hash_map={}
# hash_map["Name"]="Virat Kohli"
# hash_map["DOB"]="Nov-5"
# hash_map["Runs"]=650
# hash_map["Wickets"]=1
# hash_map["Team"]="India"
# print(hash_map)
# for i in hash_map.keys():
#     print(i)
# for i in hash_map.values():
#     print(i)
# print(hash_map["Runs"])

# st=input()
# l=list(st)
# s=""
# for i in range(len(l)):
#     if i!=len(l)-1:
#         if l[i]!=l[i+1]:
#             s=s+l[i]
#     else:
#         s=s+l[i]
# print(s)