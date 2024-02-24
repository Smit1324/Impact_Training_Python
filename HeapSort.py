# #heap sort with min heap
# def heapify(arr,n,i):
#     smallest=i #largest as root
#     l=2*i+1
#     r=2*i+2
#     if l<n and arr[l] < arr[smallest]:
#         smallest=l

#     if r<n and arr[r] < arr[smallest]:
#         smallest= r
#     #change if need
#     if smallest != i:
#         (arr[i],arr[smallest])=(arr[smallest],arr[i])
#         heapify(arr,n,smallest)

# def heapSort(arr):
#     n=len(arr)

#     for i in range(n//2-1,-1,-1):
#         heapify(arr, n, i)

#     for i in range(n-1,-1,-1):
#         (arr[i],arr[0])=(arr[0],arr[i])
#         print(i,arr)
#         heapify(arr,i,0)

# arr =[12,11,13,5,6,7]
# heapSort(arr)
# n=len(arr)
# print("sorted array: ")
# for i in range(n):
#     print(arr[i])

# heapify(arr,6,2)
# smallest=2
# l=5,r=6
# 5<6 and 7<11
# smallest=5
# 6<6 and 12<5#false
# 2!=5
# 12 5 6 11 7 13

# heapify(arr,6,5)
# smallest=5
# l=11,r=12
# 11<6 and 13<5#false
# 5!=5#false
# 12 5 6 11 7 13

# heapify(arr,6,1)
# smallest=1
# l=3,r=4
# 3<6 and 5<11
# smallest=3
# 4<6 and 6<5#false
# 1!=3
# 12 5 7 11 6 13

# heapify(arr,6,3)
# smallest=3
# l=7,r=8
# 7<6 and 11<5#false
# 3!=3#false
# 12 5 7 11 6 13

# heapify(arr,6,0)
# smallest=0
# l=1,r=2
# 1<6 and 5<12
# smallest=1
# 2<6 and 7<5#false
# 1!=0
# 5 12 7 11 6 13

# heapify(arr,6,1)
# smallest=1
# l=3,r=4
# 3<6 and 11<12
# smallest=3
# 4<6 and 6<11
# smallest=4
# 4!=1
# 5 6 7 11 12 13

# heapify(arr,5,0)
# 13 6 7 11 12 5
# smallest=0
# l=1,r=2
# 1<5 and 6<5
# smallest=1
# 2<5 and 7<6#false
# 1!=0
# 6 13 7 11 12 5
# heapify(arr,5,1)
# smallest=1
# l=3,r=4
# 3<5 and 11<13
# smallest=3
# 4<5 and 12<11#false
# 3!=1
# 6 11 7 13 12 5
# heapify(arr,5,3)
# smallest=3
# l=7,r=8
# 7<5 and 13<11#false
# 8<5 and 12<13#false
# 3!=3#false
# 6 11 7 13 12 5
