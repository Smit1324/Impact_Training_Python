# Nested If

# It is an another if condition. In nested If we have Oute If condition and Inner If condition. If outer If condition is true then only we will check the inner If condition.

# Question >> Write a program to read name of the students, roll no and 3 subject marks. If student is passed, calculate the grade of the student.

# s1,s2,s3=map(int,input("3 subs : ").split(","))
# print("s1 : ",s1,"s2 : ",s2,"s3 : ",s3);
# if((s1>35)and(s2>35)and(s3>35)):
#     total=s1+s2+s3
#     avg=total/3
#     if(avg>=60):
#         print("First Grade")
#     elif(avg>=50):
#         print("Second Grade")
#     else:
#         print("Third Grade")
# else:
#     print("FAILED!!!")

#Read a number and check if it is divisible by 3 and 5 or not
# num=int(input("Enter a number : "))
# if((num%3==0)or(num%5==0)):
#     if((num%3==0)and(num%5==0)):
#         print("Divisible by both 3 & 5")
#     elif(num%3==0):
#         print("Divisible by 3 only")
#     else:
#         print("Divisible by 5 only")
# else:
#     print("Not Divisible by both 3 & 5")

# -------------------------------------------------BREAK--------------------------------------------------------
# -------------------------------------------------BREAK--------------------------------------------------------


# Strings

# 1) It is a collection of char or array of char
# 2) String indexing starts from zero and end with n-1
# 3) We can find length of the string using len function
# 4) We can declare string in 3 ways:
#     1)Single Quotes
#     2)Double Quotes
#     3)Triple Quotes
# Strings supports both positive and negative indexing


# String indexing : Accessing a char from a string
# Slicing : Accessing sub string from a string

# s="lokesh it"
# s[2]='k'
# s[5]='h'
# s[2:5]='kes'
# s[3:8]='esh it'
# s[2:]='keh it'
# s[:6]='lokesh'
# s[::1]='lokesh it'
# s[::3]='le'
# s[::1][::2]='lks t'
# s[::1][::2][::3]='l'

# s[-2]="h it"
# s[-2:-5]=""
# s[-2:-5:-1]="i h"
# s[-2:-5:-1]="i h"
# s[::-1]="ti hsekol"
# s[2:-2]=s[2:7]="ti hsekol"
# s[:-5]=s[:4]="loke"

# s="Rohith"
# s[-2:]+s[:-2]="thRohi"

# n=int(input())
# l=list(map(int,input().split()))[:n]
# p=int(input())
# newl=l[-p::]+l[:-p]
# print(*newl)

# -------------------------------------------------BREAK-------------------------------------------------------- 
# -------------------------------------------------BREAK-------------------------------------------------------- 


# Control statements

# Python Programming supports two types of Control statements, first one is for loop & second one os while loop
# For loop is applicable for iterable objects
# The objects which contains a seq of elements that is calles as iterable objects ex all collections list, tuple,set,dictionary
# We dont apply for loop on non-iterable objects ex all fundamental data types except strings

# s="Krishna"
# for p in s:
#     print(p)
# for p in s:
#     print(p,end=" ")

# l=[2,4,6,8,10]
# for p in range(len(l)):
#     print(p,l[p])

# for p in range(2,21,2):
#     print(p, end=" ")

# str=input("Enter a string")
# pstr=str.lower()
# array="abcdefghijklmnopqrstuvwxyz"
# flag=False
# for p in array:
#     if (p not in str):
#         print(p,end=" ")
#         flag=True
# if(flag==False):
#     print("0")


# def invertWordsInSameOrder(str):
#     tok=str.split()  #["tok1","tok2",...]
#     for p in tok:
#         d=p[::-1]
#         print(d,end=" ")

# str=input() 
# invertWordsInSameOrder(str)

# Write a program to print the prime numbers between 2-50
# for p in range(2,51):
#     c=0
#     for q in range(1,p+1):
#         if(p%q==0):
#             c=c+1
#     if(c==2):
#         print(p,end=" ")

 
# for num in range(1,101):
#     factor=0
#     for p in range(1,num):
#         if (num%p==0):
#             factor=factor+p
#     if(factor==num):
        # print(num)

# n=input()
# otp=''
# l=len(n)
# for i in n:
#     i=int(i)
#     if(i%2!=0):
#         v=i*i
#         otp=otp+str(v)
# print(otp)


# While loop

# i=1
# while(i<=10):
#     print(i)
#     i+=1
# i=1
# while(i<=10):
#     if(i%2==0):
#         print(i)
#     i+=1
# i=1
# while(i<=10):
#     if(i%2!=0):
#         print(i)
#     i+=1
# i=1

# Write a program to print sum of digits 
# n=int(input())
# sum=0
# while(n!=0):
#     i=n%10
#     sum=sum+i
#     n=n//10
# print(sum)

# Write a program to check if a number is palindrome or not
# n=int(input())
# num=n
# rev=0
# while(n!=0):
#     i=n%10
#     rev=(rev*10)+i
#     n=n//10
# if(num==rev):
#     print("Its a Palindrome")
# else:
#     print("Its not a Palindrome")

# Write a ptogram to find disarium number
# n=int(input())
# l=len(str(n))
# s=0
# m=n
# while(n!=0):


