# s="lokesh it"
# s.title() //Lokesh It
# s.upper() //LOKESH It
# s.lower() //lokesh it
# s.isupper() //False
# s.islower() //Trues
# s="12345"
# s.isdigit() //True
# s="LOKESH123"
# s.isalnum() //True

# str=input()
# for i in str:
#     if(i.isdigit()):
#         print(str.index(i),end="")

# str=input()
# r=''
# for p in str:
#     if(p.isalpha()):
#         r=r+p
# r=r[::-1]
# res=''
# i=0
# for p in str:
#     if(p.isalpha()):
#         res=res+r[i]
#         i+=1
#     else:
#         res=res+p
# print(res)

# str=input()
# sp=0
# for i in str:
#     if(i.isalpha()==False and i.isalnum()==False and i.isdigit()==False):
#         sp+=1
# print(sp)

# str=input()
# r=''
# v="aeiou"
# for p in str:
#     if(p in v):
#         r=r+p
# r=r[::-1]
# res=''
# i=0
# for p in str:
#     if(p in v):
#         res=res+r[i]
#         i+=1
#     else:
#         res=res+p
# print(res)


#------------------------------------------------BREAK----------------------------------------------------------


# Lists

# Python supports four types of collections those are lists, tuples, sets & dictionaries
# All collections objects are used into store multiple values in a single variables

# List objects can be created by using [] or by calling the list fn
# This is mutable object
# Insertion order is preserved
# Duplicate elements are allowed in the lists
# List is a collection of homogeneous & heterogeneous elements
# Lists supports both indexing & slicing

# Nested lists
# A list within the another list is called as nested lists

# List Comprehension
# Using it, we can reduce no. of lines in our code
# The concept of generating elements into list objects by writing some logic 

# The concept of generating elements into list is known as list Comprehension

# l=list(range(10,110,10))
# print(l)  //[10,20,30,40,50,60,70,80,90,100]
# id(l)  //1563290436593
# l[2:5]  //[30,40,50]
# l[-2]  //90
# l[-5,-2]  //[60.70.80]

# l=[1,2,3,4,5]
# i=0
# while i<len(l):
#     print(l[i], end='')
#     i=i+1
# print()
# for p in l:
#     print(p, end='')    
# print()
# for p in range(len(l)):
#     print(l[p], p) 
# print(max(l))    
# print(min(l))
# print(sum(l))
# avg=sum(l)/len(l)
# print(avg)

# num=input()
# l=list(map(int,str(num)))
# l.sort(reverse=True)
# print(l)
# r=list(map(str,l))
# print(''.join(r))

# num=input()
# l=list(map(int,str(num)))
# l.sort()
# if(l[0]==0):
#     l[0],l[1]=l[1],l[0]
# r=list(map(str,l))
# print(''.join(r))

# Methods of List:

# insert():This method will add elemnt at specific position
# append():This method will add elemnt at the end
# extend():This method will add mutiple elements but at the end
# copy():We can copy one list to another
# count():To find how many times an element is repeated
# index():To find index of an element
# remove():To remove an element on the basis of vale
# del() and pop():To remove an element at a particular index
# sort():It will arrange the elements in ascending order/ descending order
# reverse():It will arrange the elements in reverse order
# clear():This method will clear the list

# l=[10,20,30,40,50,60]
# l.append(70) //[10,20,30,40,50,60,70]
# l.extend([10,20,30]) //[10,20,30,40,50,60,70,10,20,30]
# l.insert(2,25)  //[10,20,25,30,40,50,60,70,10,20,30]
# y=l.copy()
# l.remove(40) //[10,20,25,30,50,60,70,10,20,30]
# l.pop()  //30
# l.pop(2)  //25
# del l[2]  //[10,20,50,60,70,10,20]
# del l[2:5]  ////[10,20,10,20]
# l.index(20)  //1
# l.count(20)  //2
# d=[3,1,4,7,9,6,5]
# d.sort()  //[1,3,4,5,6,7,9]
# d.sort(reverse=True)  //[9,7,6,5,4,3,1]
# d.reverse()  //[5,6,9,7,4,1,3]
# d.clear()  //[]
# y.[2:5]=[1,2,3]  //[10,20,1,2,3,50,60,70,10,20,30]

# li=[5,1,9,"Ram","Sita",8,0,"Krishna",7]
# l=li.copy()
# newli=[]
# for i in range(len(li)):
#     if(type(li[i])==int):
#         newli.append(li[i])
#         l.remove(li[i])
# newli.sort()
# l.sort()
# for i in range(len(l)):
#     newli.append(l[i])
# print(newli)

