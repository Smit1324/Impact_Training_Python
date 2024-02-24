# # Radix Sort is a linear sorting algorithm that sorts the element by processing them digit by digit.
# # It is an efficient sorting algorithm for integers or strings in fixed sized pieces.
# # The key idea of behind the radix sort is a concept of place value.
# # It assumes that sorting numbers digit by digit will result in a fully sorted list.
# # Radix sort can be performed in two ways:
# # 1. Least Significant Digit (LSD) Radix Sort
# # 2. Most Significant Digit (MSD) Radix Sort

# # Algorithm Working : 
# # 1. Find the largest element in the array. [170,45,75,90,802,24,2,66]
# #     l=802
# # 2. Count the number of digits in it.
# #     3
# # 3. Sort the elements based on the digit at the unit place.
# #     We use a stable sorting technique such as Counting Sort to sort the digits at each significant places.
# #     170,90,802,2,24,45,75,66
# # 4. Sort the elements based on the digit at the tens place.
# #     802,2,24,45,66,170,75,90
# # 5. Sort the elements based on the digit at the hundreds place.
# #     2,24,45,66,75,90,170,802
# # 6. The array is sorted in ascending order.
# #     2,24,45,66,75,90,170,802

# # l=[192,45,62,78,5,9,675,902,23]
# # [192,45,62,78,5,9,675,902,23]
# # max=902
# # digits_count=3
# # Sorting based on one's value : [192,62,902,23,45,675,5,78,9]
# # Sorting based on ten's value : [902,5,9,23,45,62,675,78,192]
# # Sorting based on hundred's value : [5,9,23,45,62,78,192,675,902]
# # [5,9,23,45,62,78,192,675,902]

# def countingSort(arr,exp):
#     n=len(arr)
#     output=[0]*n
#     count=[0]*10
#     for i in range(0,n):
#         index=(arr[i]//exp)
#         count[index%10]+=1
#     for i in range(1,10):
#         count[i]+=count[i-1]
#     i=n-1
#     while i>=0:
#         index=(arr[i]//exp)
#         output[count[index%10]-1]=arr[i]
#         count[index%10]-=1
#         i-=1
#     i=0
#     for i in range(0,len(arr)):
#         arr[i]=output[i]
#     return arr

# def radixSort(arr):
#     max1=max(arr)
#     exp=1
#     while max1//exp>0:
#         arr=countingSort(arr,exp)
#         exp*=10
#     return arr

# arr=[170,45,75,90,802,24,2,66]
# n=len(arr)
# arr=radixSort(arr)
# print("Sorted array is: ")
# for i in range(n):
#     print(arr[i],end=" ")

