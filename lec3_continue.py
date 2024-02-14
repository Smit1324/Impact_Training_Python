# Write a program to read list from user with & without using for loop
# l=list(map(int,input().split()))
# print(l)
# n=int(input())
# r=[]
# for p in range(n):
#     val=int(input())
#     r.append(val)
# print(r)

# n=int(input())
# l=list(map(int,input().split()))
# l.sort()
# r=[]
# for p in range(len(l)//2):
#     r.append(l[p])
#     r.append(l[-p-1])
# if len(l)%2!=0:
#     r.append(l[len(l)//2])
# print(r)


# n=int(input())
# l=list(map(int,input().split()))
# r=[]
# for i in l:
#     if(i not in r):
#         r.append(i)
# print(r)

# num=int(input())
# l=list(map(int,str(num)))
# ev=[]
# od=[]
# for i in l:
#     if i%2==0:
#         ev.append(i)
#     else:
#         od.append(i)
# r=[ev.append(p) if(p%2==0) else ol.append(p) for p in l]
# ev.sort()
# od.sort()
# ev.reverse()
# ol=od+ev
# st=list(map(str,ol))
# print(''.join(st))


# inp=input()
# l=len(inp)
# a,b=1,0
# i=1
# r=[]
# while(i<=l):
#     c=a+b
#     r.append(c)
#     a=b
#     b=c
#     i=i+1
# res=''
# d=str(sum(r))
# res=res+d
# for p in range(len(inp)):
#     res=res+inp[p]+str(r[p])
# print(res)

# l=list(map(int,input().split()))
# n=int(input())
# c=l.count(n)
# for i in range(c):
#     l.remove(n)
# print(l)

# n=int(input())
# l=[]
# c=0
# for i in range(n):
#     v=input()
#     l.append(v)
# for i in l:
#     age=i[-4]+i[-3]
#     if (int(age)>=60):
#         c+=1
#         print(i[:10])
# print(c)

# n=int(input())
# l = list(map(int, input().split()))[:n]
# flag=False
# lead=0
# for i in range(n):
#     for j in range(i+1,n):
#         if(l[i]>l[j]):
#             flag=True
#         else:
#             flag=False
#             break
#     if(flag==True):
#         lead+=l[i]

# lead+=l[-1]
# print(lead)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------



# DICTIONARY

# Dictionary is a collection of Key & Value pair and one key & value pair is called an item
# Dictionary objects can created by using curly braces {} by calling dict fn
# Dictionary is a mutable object
# Insertion order is preserved
# Indexing is not supported
# Duplicate keys are not allowed
# Duplicate values are allowed
# Dictionary is a collection of homogeneous & heterogeneous keys and values
# Slicing is not supported

# d={}
# type(d)  //dict
# d={'a':10,'b':20,'c':30}  //{'a':10,'b':20,'c':30}
# d['a']  //10
# d['a']=60  //{'a':60,'b':20,'c':30}
# d[0]  //Error

# e={"Name":"Raj","id1":101, "Dept":20, "Salary":70000}
# print(e)
# print(e["Dept"])
# d=e.get("Salary")
# print(d)
# e["Salary"]=80000
# print(e)
# e["subject"]="python"
# print(e)
# for p in e.keys():
#     print(p)
# for p in e.values():
#     print(p)
# for p,q in e.items():
#     print(p,q)        
# for s in e.items():
#     print(s)


# DICTIONARY COMPREHENSION

# Th concept of generating dict objects by writing some logic in dict is known as dictionary comprehension
# By using the dictionary comprehensuion, we can reduce no. of lines in our code

# Write a program to print the square of the given number from 1 to 20 in the form of dictionary object

# d={p:p*p for p in range (1,21) if(p%2==0)}
# print(d)

# To print cubes of odd no. from 30 to 50

# d={p:p*p*p for p in range (30,51) if(p%2!=0)}
# print(d)


# x="Hyderabad"
# d={p:x.count(p) for p in x}
# print(d)

# st=input()
# v="aeiou"
# d={p:st.lower().count(p) for p in st if p in v}
# print(d)

# st=input()
# newst=''
# x=input()
# d={p:st.count(p) for p in st}
# m=max(d.values())
# k=''
# for p,q in d.items():
#     if q==m:
#         k=p
# for p in st:
#     if p==k:
#         newst=newst+x
#     else:
#         newst=newst+p

# print(newst) 


# st=int(input())
# l=list(map(int,input().split()))[:st]
# nl=[]
# d={p:l.count(p) for p in l}
# for i,j in d.items():
#     if i==j:
#         nl.append(i)
# if(nl==[]):
#     print("-1")
# else:
#     print(max(nl))


# n=int(input())
# d={}
# for i in range(n):
#     k=input()
#     v=int(input())
#     d[k]=v
# r=sorted(d.keys())
# nd={}
# for i in r:
#     nd[i]=d[i]
# print(nd)
# r=sorted(d.values())
# nd={}
# for i in r:
#     for p,q in d.items():
#         if(q==i):
#             nd[p]=q
# print(nd)


# NESTED DICTIONARY

# A dictionary within the another dict is called as nested dict

# d={"Krishna":[23,21,24],"Raju":[29,40,18],"Saritha":[22,40,16]}
# for p,q in d.items():
#     print(p)
#     s=sum(q)
#     avg=s/len(q)
#     print("Avg : %.2f"%avg)


# n=int(input())
# d={}
# for i in range(n):
#     st=input()
#     l=st.split(" ")
#     d[l[0]]=[int(l[1]),int(l[2]),int(l[3])]
# name=input()
# for p,q in d.items():
#     if p ==name:
#         s=sum(q)
#         avg=s/len(q)
#         print("Avg : %.2f"%avg)


# d={"Krishna":{"Python":23,"C":34,"Cpp":49},"Raju":{"Python":45,"C":78,"Cpp":22}}
# for i,j in d.items():
#     print(i)
#     for p in j.values():
#         print(p)
#     print("---------")


# STRING METHODS

# String Methods:-    
# s="Good Morning all"
# r=s.split()
# print(r)
# for p in r:
#     print(p) 

# s=["Good","Morning","all"]
# r='-'.join(s)
# print(r)
# r=" ".join(s)
# print(r)

# s="Dainik Bheda"
# r=s.count('a')
# r=s.index('a')
# r=s.find("a")
# r=s.rfind("a")
# r=s.replace("a","A")
# print(r)

# w="Modi is the PM of India"
# print(w)
# r=w.replace("Modi","Narendra Modi")
# print("After change:",r)

# s=" Mumbai, Maharashtra " #strip() method is used to remove the spaces from the string
# r=s.strip()
# r2=s.isspace()
# print(r)

# Write a program to read string from a user and find reverse of a string and check wether its a palindrome or not

# s=input()
# r=''
# for i in range(len(s)-1,-1,-1):
#     r=r+s[i]
# if (s==r):
#     print("ha bhaiiiii")
# else:
#     print("Na bhaiiiii")

# s=input()
# v="aeiou"
# vc=0
# cc=0
# for i in s:
#     if i in v:
#         vc+=1
#     elif i==" ":
#         continue
#     else:
#         cc+=1
# print("Vowels : ",vc)
# print("Consonants : ",cc)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# SET

# Set objects can be created by using {} are by calling set() function.
# set is a mutable object.
# duplicate elements are not allowed in Sets.
# insertion order is not preserved.
# set does not support indexing and slicing.
# set is a collection of homogeneous and heterogeneous elements.    
# set is mainly used to perform the mathematical operations like union, intersection, difference, symmetric difference, subset, superset, disjoint, etc.

# s=set()
# s=[12,23,34.45]
# s  //[12,23,34,45]
# s[2]  //Error
# s.add(35)
# s  //[34,35,23,12,45]

# s=input()
# r=set(s)
# l=list(r)
# l.sort()
# res=''
# for p in l:
#     res=res+p+str(s.count(p))
# print(res)

# s=input()
# r=set(s)
# l=list(r)
# l.sort()
# res=''
# for p in l:
#     c=s.count(p)
#     if(c>1):
#         print(p,"-",c,end=" ")

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# print(a^b)


# n=int(input())
# l=list(map(int,input().split()))[:n]
# n=int(input())
# r=list(map(int,input().split()))[:n]
# s1=set(l)
# s2=set(r)
# print(s1,s2)
# s3=s1^s2
# for p in s3:
#     print(p)

# s={1,2,3,4,5}
# s.add(6)
# print(s)
# s.remove(4)
# print(s)
# s.discard(4)
# print(s)
# s.remove(4)
# print(s)  //Error

# s={'a':10,'b':20,'c':30}
# r=s.update({'d':40})
# r2=s.update({'d':50,'e':60})
# r3=s.pop('a')    
# r5=s.clear()
# print(r,r2,r3,r5,sep="\n")

# s1=input()
# s2=input()
# set1=set(s1)
# set2=set(s2)
# d1=sorted(set1 & set2)
# d2=''.join(d1)
# print(d2)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# TUPLE

# Tuple objects can be created by using () by calling the tuple fn
# By assigning more than one value to single variable, tuple objects can be created
# Tuple is immutable objects
# Insertion order is preserved
# Duplicate elements are allowed
# Tuple supports both indexing and slicing
# Tuple is a collection of homogeneous & heterogeneous elements

# t=tuple(range(1,11))
# t  //(1,2,3,4,5,6,7,8,9,10)
# t=(1,2,3,4,5,1,2)  ////Duplicate elements are allowed
# t[2]  //3
# t[2]=11  //ERROR

# n=int(input())
# bi=""
# if n==0:
#     print("0")
# while n>0:
#     bi=str(n%2)+bi
#     n//=2
# print(bi)



#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# FUNCTION

# Function is a sub program & performs a specific operation
# A self contained block of one or more statements
#Advantages : 
    #Reusability : Writing the code only once but we can use more than once
    #Understanding the logic becomes easy
    #In python programming, we can define a fn using "def" keyword
    #Functions are divided into four types
        #Without args and without return type
        #With args and without return type
        #Without args and with return type
        #With args and with return type (Rarely used)

# Examples

#Type - 1
#def even_odd():
#     n=int(input("Enter your number: "))
#     if(n%2==0):
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# even_odd()

#Type - 2
#def even_odd(n):
#     if(n%2==0):
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# n=int(input("Enter your number: "))
# even_odd(n)

#Type - 3
#def even_odd():
#     n=int(input("Enter your number: "))
#     if(n%2==0):
#        return "Even"
#     else:
#         return "Odd"
# print(even_odd())

#Type - 4
#def even_odd(n):
#     if(n%2==0):
#        return "Even"
#     else:
#         return "Odd"
# n=int(input("Enter your number: "))
# print(even_odd(n))


# def answer_dede(p):
#     w=10**(ord(p)-ord('A'))
#     return w

# a=input()
# u=a.upper()
# s=0
# for p in u:
#     r=answer_dede(p)
#     s+=r
# print(s)


# def check_palindrome(i):
#     r=i[::-1]
#     if i==r:
#         return 1
#     else:
#         return 0    

# n=int(input())
# s=input()[:n]
# t=s.split()
# flag=False
# for i in t:
#     if check_palindrome(i) ==1:
#         flag=True
#     else :
#         flag=False

# if flag==True:
#     print("Yes")
# else:
#     print("No")



#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# LAMBDA
# 
# Lambda/Anonymous fn is a special fn in python which don't have any name
# Using lambda Function, we can reduce no. of lines in our code
# Lambda is called as higher order fn


# s=lambda a,b:a+b
# r=s(10,5)
# print(r)

# s=lambda x:x%2==0
# l=[1,2,3,4,5]
# r=[p for p in l if s(p)]
# print(r)


# s=lambda x:x%2!=0
# r=[p for p in range(30,51) if s(p)]
# print(r)

# import math
# f=lambda n: math.factorial(n)
# n=int(input())
# print(f(n))


# def cal(a, b,s):
#     r=s(a, b)
#     return r

# s1=cal(10, 5,lambda a,b:a+b)
# s2=cal(10, 5,lambda a,b:a-b)
# s3=cal(10, 5,lambda a,b:a*b)
# print(s1,s2,s3)

# def cal(f, a, b):
#     return f(a, b)

# add = lambda a, b: a + b
# sub = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b if b != 0 else 'Error: Division by zero'

# print(cal(add, 10, 5))
# print(cal(mul, 10, 5))
# print(cal(div, 10, 5))
# print(cal(sub, 10,5))


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# MAP & FILTER FUNCTION

# Filter requires a condition but map requires a expression

# with filter and without lambda    
# def even(n):
#     return n%2==0
# l=list(range(10,31))
# r=list(filter(even,l))
# print(r)

# # with filter and lambda
# l=list(range(10,31))
# r=list(filter(lambda n:n%2==0,l))
# print(r)


# def pos(n):
#     return n>0
# def neg(n):
#     return n<0

# l=list(range(-5,6))
# n=list(filter(neg,l))
# p=list(filter(pos,l))

# n=list(filter(lambda x:x<0,l))
# p=list(filter(lambda x:x>0,l))
# print(n,'\n',p)

# l=["abc","ABC","xyz","XYZ","aBc"]
# r=list(filter(lambda x:x.isupper(),l))
# print(r)

# s=["abc","xyz"]
# r=list(map(lambda x:x.upper(),s))
# print(r)


# REDUCE FUNCTION

# It is a fn, it is imported from functools module

# from functools import reduce
# s=[1,2,3,4,5]
# # r=reduce(lambda x,y:x+y,s)
# # print(r)

# m1=reduce(lambda x,y:x if x<y else y,s)
# m2=reduce(lambda x,y:x if x>y else y,s)
# print(m1,m2)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# ITERATOR

# Using iterator, we can return only one value at a time

# ENUMERATOR

# It will return the value along with the count
# The default count starts from 0

# GENERATOR

# The return stat can return only one value at a time
# The generator can return multiple values
# Generator internally use yield and next method for returning multiple values

# l=[1,2,3,4,5]
# r=iter(l)
# next(r)

# l=[1,2,3,4,5]
# r=enumerate(l)
# next(r)

# def gen():
#     yield 5
#     yield 10
#     yield 15
#     yield 20
# g1=gen()
# r=next(g1)
# r1=next(g1)
# r2=next(g1)
# r3=next(g1)
# print(r,r1,r2,r3)

# def gen():
#     l=[1,2,3,4,5]
#     for p in l:
#         yield p
# g1=gen()
# for i in g1:
#     print(i)

# Note : In python programming, you can generate random numbers using random functions

# import random
# s=random.randint(1000,9999)
# print(s)

# Write a program to generate four random OTPs within the range of 1000 to 10000

# import random

# def gen():
#     for i in range(4):
#         s=(random.randint(1000,9999))
#         yield s
# g1=gen()
# for p in g1:
#     print(p)

# import math # using yield and for loop and predefined functions.
# def gen():
#     for i in range(5,10):
#         yield math.factorial(i)  
# g1=gen()
# for p in g1:
#     print(p) 
    
# def fact(s, e): # using yield and for loop and no any predefined functions.
#     for i in range(s, e+1):
#         f=1
#         for j in range(1,i+1):
#             f=f*j
#         yield f
# g=fact(5,10)
# for p in g:
#     print(p)   

# l=[1,2,3,4,5] # enumerator
# r=iter(l)
# for p in r:
#     print(p)   
    
# l=[1,2,3,4,5]
# r=enumerate(l)
# for p in r:
#     print(p)    

# Closures:
#     closure is a special function. 
#     closure are developed by using nested functions.
#     closure is inner function, which performs some operations using the data of outer function even outer function execution completed. 
    
# Decorators:
#     decorator is a special function.
#     decorator function receives input as one functions and return another function as output.
#     a functuion returing another function, usually applied as a function transforamtion using the @wrapper syntax. Common examples for decorators  are classmethod() and staticmethod().
#     decorators are used to add new features to the existing functions or extending functionalities of the existing functions without modifying it. 
#     Decorators can be developeed irrespective of functionality.  
    
# def power(p):
#     def pow(n):
#         return p**n
#     return pow
# s=power(5)
# p=s(2)  
# print(p)
# s1=power(4)
# p1=s1(3)  
# print(p1) 

# def p(s):  # code to print **** and $$$$$ using of closures def ke andar def
#     def w(n):
#         return s * n
#     return w
# p1=p('*')
# p2=p('$')
# print(p1(10))
# print(p2(10))

# def new_display(d):
#   def smart_display():
#     print("****************")
#     d()
#     print("****************")
#   return smart_display

# @new_display
# def display():
#   print("python Programming")
# display()

# def smart_div(d):
#     def division (a,b):
#         if b==0:
#             return 0
#         else:
#             return d(a,b)
#     return division
# @smart_div
# def div(a,b):
#     return a/b
# a=div(10,2)
# print(a)
# a=div(10,0)
# print(a)

# def smart_div(d):
#     def division (a,b):
#         if type(b)==str:
#             return "Division by string not possible"
#         else:
#             return d(a,b)
#     return division
# @smart_div
# def div(a,b):
#     return a/b
# a=div(10,2)
# print(a)
# a=div(10,"abc")
# print(a)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# LIST COMPREHENSION

# The concept of generating elements into list objects by writing some logic into list is known as List comprehension
# By using it, we can reduce no. of lines in our code

# l=[p for p in range(1,11)]
# print(l)

# l=[p for p in range(1,21) if p%2==0]
# print(l)

# l=[int(input()) for p in range(5)]
# print(l)

# l=[x*x for x in range(30,50) if x%2!=0]
# print(l)

# NESTED LIST

# A list within the another list is called as Nested List

# l=[[1,2,3],[4,5,6],[7,8,9]] 
# print(l)
# for p in l:
#     print(p)
#     print('-----')
#     for q in p:
#         print(q)

# l=[]
# for p in range(3):
#   l1=[]
#   for q in range(3):
#     val=int(input())
#     l1.append(val)
#   l.append(l1)
# print(l)

# n=int(input())
# l=list(map(int,input().split()))[:n]
# print(l)
# l.sort()
# c=l.count(l[0])
# d=l[c]
# print("Second Min : ",d)
# c1=l.count(l[-1])
# d1=l[-(c1+1)]
# print("Second Max : ",d1)

# l=[[int(input()) for i in range(3)] for i in range(3)]
# print(l)

# l1=[[int(input()) for i in range(2)] for i in range(2)]
# print()
# l2=[[int(input()) for i in range(2)] for i in range(2)]
# s=[[0,0],[0,0]]
# for i in range(2):
#     for j in range(2):
#         s[i][j]=l1[i][j]+l2[i][j]
# for i in range(2):
#     for j in range(2):
#         print(s[i][j],end=" ")
#     print()

# l=[[int(input()) for i in range(3)] for i in range(3)]
# print()
# s=[0,0,0]
# for i in range(3):
#     for j in range(3):
#         s[i]+=l[i][j]

# print(s)

# l=[[int(input()) for i in range(3)] for i in range(3)]
# print()
# s=[0,0,0]
# for i in range(3):
#     for j in range(3):
#         s[i]+=l[j][i]

# print(s)


#---------------------------------------------------BREAK--------------------------------------------------------
#---------------------------------------------------BREAK--------------------------------------------------------


# EXCEPTION HANDLING

# In python programming, there are two types of errors:
#     Compile time Errors : Errors occuring at compilation time.
#                         This kind of errors should be handled by user
#     Runtime Errors : Errors occuring at runtime.
#                     Becuz of runtime errors, the program will be terminated abnormally
#                     We can handle the exceptions with the help of try and except block

#     Try block : The statements which produce an exception & the other statements which depends on the exception, we have to keep inside the try block.

#     Except block : We have to pass corresponding exception classname as an argument to except block
#         Generally user friendly error meassages will be given in the except block


# print("start")
# a=int(input("Enter a value: "))
# try:
#     b=int(input("Enter b value: "))
#     c=a/b
#     print(c)
# except(ZeroDivisionError):
#     print("Division by zero not possible")
# print("end")

# Different Types of Exception:
#     ZeroDivisionError : 
#     ValueError 
#     TypeError 
#     IndexError 
#     KeyError
#     NameError 
#     AttributeError 
#     ArrayOutOfBoundException
#     Raise error

# def ra(n):
#     assert ((n>3) and (n<=15),"Specified range")
#     print("Entered number",n)
# try:
#     n=int(input("Enter a num : "))
#     ra(n)
# except(AssertionError):
#     print("Range is b/w 3 and 15")


# RAISE

# We can raise our own error using the raise error if the given condition is not satisfied then this error will be raised.

# Que>> After withdraw operation, the balance is less than 1500 INR then we have to raise the error


# bal=4000
# def withdraw(amt):
#     global bal
#     if(bal-amt)<1500:
#         raise ValueError
#     else:
#         print("Balance : ",bal-amt)
# try:
#     amt=int(input("Enter Amount : "))
#     withdraw(amt)
# except:
#     print("Maintain a min balance of 1500")


#---------------------------------------------------BREAK-------------------------------------------------------
#---------------------------------------------------BREAK-------------------------------------------------------

# MODULE

# In python programming, we have two types of module
#     Normal Input
#     From Input
# Using the module transact, we can access the properties of 1 python file inside another python file
# We can access the properties of one py file to another
# In real world scenario, one application is a collection of program
# So, two programs will communicate each other by module concept only
# Sending and receiving the values
# 

# import testt
# import math
# b=200
# def m2():
#     print("in m2 : ")
# print(b)
# m2()
# print(testt.a)
# testt.m1()
# print(math.pi)
# f=math.factorial(5)
# r=math.sqrt(100)
# print(f,r)

# from testt import *
# from math import *
# b=200
# def m2():
#     print("in m2 : ")
# print(b)
# m2()
# print(a)
# m1()
# print(pi)
# f=factorial(5)
# r=sqrt(100)
# print(f,r)


#---------------------------------------------------BREAK-------------------------------------------------------
#---------------------------------------------------BREAK-------------------------------------------------------


# FILE HANDLING

# files are used to store the data permanently 
# we can perform different operation in our files such as we can open the file, we can update the file, read the data from the file, write the data in the file and we can append the data in the file and finnaly close the opened file
# Different modes available 
# r - indicates the read operation
# w - indicates the write operation
# a - indicates the append operation
# r+ - indicates both read & write operation
# w+ - indicates both write & read operation
# a+ - indicates both append & read operation


# from demo11 import*
# a,b=map(int,input().split())
# s1=add(a,b)
# s2=sub(a,b)
# s3=mul(a,b)
# print(s1,s2,s3)

# Reading data from the file

# x=open("C:/Users/hplap/OneDrive/Desktop/hi.txt")
# print(x.read())
# x.close()

# Writing data from the file

# x=open("C:/Users/hplap/OneDrive/Desktop/hi.txt",'w')
# x.write("Ye kya kar dala mene")
# print("Data written successfully")
# x.close()

#Appending data into the file

# x=open("C:/Users/hplap/OneDrive/Desktop/hi.txt",'a')
# x.write("Kora kagaz tha ye mann meraa \n Likh diya uspe naam teraa")
# print("File updated successfully")
# x.close()

# r+ mode operation

# x=open("C:/Users/hplap/OneDrive/Desktop/hi.txt",'r+')
# print(x.read())
# x.write("Kora kagaz tha ye mann meraa \nLikh diya uspe naam teraa")
# print('\n')
# print(x.read())
# x.close()


#---------------------------------------------------BREAK-------------------------------------------------------
#---------------------------------------------------BREAK-------------------------------------------------------

# RECURSION 

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input())
# print(fact(n))

# def summation(n):
#     if n==0:
#         return 0
#     else:
#         return n+summation(n-1)
# print(summation(5))


#---------------------------------------------------BREAK-------------------------------------------------------
#---------------------------------------------------BREAK-------------------------------------------------------