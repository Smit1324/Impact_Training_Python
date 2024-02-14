# --> In the binary serach first we have to sort the elements.
# --> calculate low and high values,that's is low = 0 and high = len(l)-1.
# ---> calculate the mid index position i.e, (low + high )/2 , based on the mid position find the middle value in the list and comapre middle value with the key value , if middle values is     less than key value then incriement the low , if middle values is greater than key values then decrement the high value with 1, if two condition are not satisified that will be indicated as middle value and key values are equal then return the index position.

# --> If the element is not available then this algorithm will return -1.


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# #Sorting algorithm in python:-
# -----------------------------

# ~> Python supports different sorting algorithm (seven - algorithm)
# 1) Bubble sort
# 2) Selection sort
# 3) Insertion sort
# 4) Merge sort
# 5) Qucik sort
# 6) Radix sort (frequency sort)
# 7) heap sort

# 1) Bubble sort:-

# --> Bubble sort is worst sorting algorithm as comapre to all sorting algorithm.
# --> In bubble sort we have to comapre the adjacent elements , if the elements are not sorted then we have to sort.
# --> bubble sort will arrange the elements in ascending order or descending order
# ---> For ascending order we have to use greater than symbol and for lesser one we have to lesser than or equal to symbol.


# def bubble_sort(l):
#     flag=False
#     for p in range(len(l)-1):
#         for q in range(len(l)-1):
#             if(l[q]>l[q+1]):
#                 l[q],l[q+1]=l[q+1],l[q]
#                 flag=True
#         if flag==False:
#             break
#     return l

# l=list(map(int,input().split()))
# print("Bubble Sort",l)
# s=bubble_sort(l)
# print("After Sort",s)


# def bubble_sort(l):
#     flag=False
#     for p in range(len(l)-1):
#         for q in range(len(l)-1):
#             if(len(l[q])>len(l[q+1])):
#                 l[q],l[q+1]=l[q+1],l[q]
#                 flag=True
#         if flag==False:
#             break
#     return l

# l=list(map(str,input().split()))
# print("Bubble Sort",l)
# s=bubble_sort(l)
# print("After Sort",s)


# SELECTION SORT

# In the Selection Sort, the first element will be consider as min element in the list, then remaining all the elements will be compared with the first element, If any element is less than the min element then first we are going to exchange the index position of min element. After all comparisions, the min value will removed to sorting location

# def selection_sort(l):
#     for i in range(len(l)):
#         min_index=i
#         for j in range(i+1,len(l)):
#             if l[min_index]>l[j]:
#                 min_index=j
#         l[min_index],l[i]=l[i],l[min_index]
#     return l

# l=list(map(str,input().split()))
# print("Before Sort",l)
# s=selection_sort(l)
# print("After Sort",s)

# 9 4 1 8 3 5
# 1 4 9 8 3 5
# 1 3 9 8 4 5
# 1 3 4 8 9 5
# 1 3 4 5 9 8
# 1 3 4 5 8 9


# MERGE SORT

# Merge sort works on the principle of divide and conquer.
# First we have to divide the list into two equal parts that is len()//2, this division is possible until the length is equal to 1.
# For didviding the elements into equal parts we are using recursion technique.
# During comparision, we are going to compare left side value with the right side value, if left side value is less than right side value then left side value will come first, if condition is false, right side value will come first.

# 40 60 30 50 10 20
# 40 60 30        50 10 20
# 40      60 30      50       10 20
# 40      60      30      50      10      20
# 40      30      60      10      50      20
# 30      40      60      10      20      50
# 10      40      60      30      20      50
# 10      20      60      30      40      50
# 10      20      30      40      50      60

# 3 1 9 2 7 5
# 3 1 9   2 7 5
# 1 3 9   2 5 7
# 1
# 3 9     2 5 7
# 1 2
# 3 9     5 7
# 1 2 3
# 9       5 7
# 1 2 3 5
# 9       7
# 1 2 3 5 7 9

# 5 2 1 9 6 3
# 5 2 1   9 6 3
# 1 2 5   3 6 9
# 1
# 2 5     3 6 9
# 1 2
# 5       3 6 9
# 1 2 3
# 5       6 9
# 1 2 3 5
#         6 9
# 1 2 3 5 6
#         9
# 1 2 3 4 5 6 9

# def merge(left,right):
#   merged=[]
#   i = 0
#   j = 0
#   while((i<len(left)) and ((j<len(right)))):
#     if(left[i]<right[j]):
#       merged.append(left[i])
#       i = i+1
#     else:
#       merged.append(right[j])
#       j=j+1
#   merged = merged + left[i:] + right[j:]
#   return merged
  

# def merge_sort(l):
#   if(len(l)==1):
#     return l
#   else:
#     mid = len(l)//2
#     left=merge_sort(l[:mid])
#     right=merge_sort(l[mid:])
#     return merge(left,right)


# l=list(map(int,input().split()))
# print("Before sort",l)
# s=merge_sort(l)
# print("After Sort",s)

# INSERTION SORT

# def insertion_sort(l):
#     for p in range(1,len(l)):
#         key=l[p]
#         q=p-1
#         while((q>=0)and(key<l[q])):
#             l[q+1]=l[q]
#             q=q-1
#         l[q+1]=key
#         print(l)
#     return l
# l=[5,4,1,2,3]
# print("Before sort",l)
# s=insertion_sort(l)
# print("After sort",s)


# 5 4 1 2 3
# 4 5 1 2 3
# 1 4 5 2 3
# 1 2 4 5 3
# 1 2 3 4 5

# s=input()
# v="aeiouAEIOU"
# count=0
# for i in range(len(s)):
#     if s[i] in v:
#         if i!=len(s)-1:
#             if (ord(s[i+1].lower()) in range(97,123)) and s[i+1] not in v:
#                 count+=1
# print(count)

# QUICK SORT

# Consider the first element of the array as the pivot element.
# Initialize i to low & j to high.
# Increment i till the element at i is less than the pivot element.
# Decrement j till the element at j is greater than the pivot element.
# If i is less than j, swap the elements at i and j.
# If i is greater than j, swap the pivot element with the element at j.
# Repeat the above steps for the sub-arrays on the left and right of the pivot element.
# Time Complexity: O(nlogn) in average case and O(n^2) in worst case

def quick_sort(l,low,high):
    if low<high:
        pi=partition(l,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return l

def partition(l,low,high):
    pivot=l[low]
    i=low
    j=high
    while(i<j):
        while(i<len(l) and l[i]<=pivot):
            i+=1
        while(l[j]>pivot):
            j-=1
        if i<j:
            l[i],l[j]=l[j],l[i]
    l[low],l[j]=l[j],l[low]
    return j

l=list(map(int,input().split()))
print("Before sort",l)
s=quick_sort(l,0,len(l)-1)
print("After sort",s)