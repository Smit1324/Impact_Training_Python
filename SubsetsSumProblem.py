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