# OBJECT ORIENTED PROGRAMMING

# In procedure oriented programming, we are declaring the data as a global then related functions as well as unrelated functions also will acess the data, then we are loosing security for our data.
# We can achieve the security with the help of object oriented programming.
# Object oriented programming, principles are :
#     Class : 
#             Class is a container which contains data & data related operations in single entity.
#             Class is a collection of data members & member functions.
#             Class is a collection of variables and methods.
#             Data can be represented by variables and operations are represented by methods.
#             Within a class, we can declare 3 types of variables : 
#                 Static variable
#                 Non static variable
#                 Local variable
#             We can 3 types of methods within a class:
#                 Static method
#                 Non-static method
#                 Class method
#     Object : 
#             Object is an instance of a class i.e., by creating objects, memory will be alloted for the data members of a class
#             When class is created memory will be alloted for the static variables and static methods.
#             When object is created, memory will be alloted for the non static variables and non static methods.
                # Static Variable : 
                                # The variables which are declared within a class but outside of all the methods, those variables are called Static variables.
                                # We can access static variables within a class by using the classname and outside of a class by using the classname and object name.
                                # If the data is common to all objects, then we can declare those variables as Static variables.
                                # For static variables, memory is alloted when the class is loaded
                # Non Static Variable : 
                                # The variables which are declared within a class and within a methods, those variables are called Non Static variables.
                                # We can acess a non static variable within a class using self keyword and outside of a class using by using object name.
                                # If the data change from object to object, we can declare the variable as Non Static variable.
                # Non Static Method : 
                                # We can access the non static method by using object name.
                                # For non static method, memory is alloted when an object is created.
                # Static Method :
                                # We can access the static method by using class name.
                                # No object creation is required
#     Encapsulation
#     Inheritance
#     Polymorphism
#     Abstraction & Interfaces

# st=input()
# flag=False
# for i in st:
#     if st.count(i)==1:
#         print(i)
#         break
#     else:
#         flag=True
# if(flag):
#     print("Either all characters are repeating or the string is empty")

# class test:
#     a=1000
#     b=2000
#     def display(self):
#         print(test.a,test.b)
#     def update(self):
#         test.a=test.a+10
#         test.b=test.b+20
# t1=test()
# t1.display()
# t1.update()
# t2=test()
# t2.display()
# t2.update()
# t2.display()

# class test: 
#     def insert(self):
#         self.a=1000
#         self.b=2000
#     def display(self):
#         print(self.a,self.b)
#     def update(self):
#         self.a=self.a+10
#         self.b=self.b+20
# t1=test()
# t1.insert()
# t1.display()
# t1.update()
# t1.display()
# t2=test()
# t2.insert()
# t2.display()

# class test: 
#     def insert(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a,self.b)
# t1=test()
# t1.insert(10,20)
# t1.display()
# t2=test()
# t2.insert(30,40)
# t2.display()

# CONSTRUCTOR

# It is a special type of method.
# We can define a constructor in python programming by using __init__.
# Constructor is removed automatically during creation objects.
# We have 2 types of constructor : 
#     Default Constructor
#     Parameterised Constructor

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def display(self):
#         print(self.a,self.b)

# t1=test()
# t1.display()

# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         print("Area :",3.14*self.r*self.r)
# n=int(input())
# a=circle(n)
# a.area()

# class rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print("Area :",self.l*self.b)
# n1=int(input())
# n2=int(input())
# a=rectangle(n1,n2)
# a.area()


# class student:
#     def __init__(self,name,rollno,address,sub1,sub2,sub3):
#         self.name=name
#         self.rollno=rollno
#         self.address=address
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def display(self):
#         print("Name of a student is: ", self.name)
#         print("Rollno of a student is: ",self.rollno)
#         print("Address of a student is: ",self.address)
#         print("Marks of subject1 is: ",self.sub1)
#         print("Marks of subject2 is: ",self.sub2)
#         print("Marks of subject3 is: ",self.sub3)
        
#     def update(self):
#         self.total=self.sub1+self.sub2+self.sub3
#         self.avg=self.total/3
#         if(self.sub1>=35 and self.sub2>=35 and self.sub3>=35):
#             print("Pass")
#             if(self.avg>=75):
#                 print("Grade A")
#             elif(self.avg>=60 and self.avg<75):
#                 print("Grade B")
#             elif(self.avg>=50 and self.avg<60):
#                 print("Grade C")
#             elif(self.avg>=35 and self.avg<50):
#                 print("Grade D")
#         else:
#             print("Fail")

# name=input("Enter the name of a student: ")
# rollno=int(input("Enter the rollno of a student: "))
# address=input("Enter the address of a student: ")
# sub1=int(input("Enter the marks of subject1: "))
# sub2=int(input("Enter the marks of subject2: "))
# sub3=int(input("Enter the marks of subject3: "))

# s1=student(name,rollno,address,sub1,sub2,sub3)
# s1.display()
# s1.update()

# class cust():
#     bank_name="HDFC"
#     def _init_(self, name, accno, bal, add):
#         self.name=name
#         self.accno=accno
#         self.bal=bal
#         self.add=add
#     def display(self):
#         print(cust.bank_name, self.name, self.accno, self.bal, self.add)
#     def check_bal(self):
#         print("Balance is: ",self.bal)
#     def deposit(self,amt):
#         self.bal=self.bal+amt
#     def withdraw(self,amt):
#         if(amt<=self.bal):
#             if(self.amt-amt>=2000):
#                 self.bal=self.bal-amt
#             else:
#                 print("Insufficient funds")
#         else:
#             print("Insufficient funds")
# c1=cust("Raj", 1234, 10000, "Hyd")
# c1.display()
# c1.check_bal()
# c1.deposit(50000)
# c1.check_bal()
# c1.withdraw(2000)
# c1.check_bal()
# c1.withdraw(10000)
# c1.check_bal()

# class book:
#     lname="pl"
#     def __init__(self,bname,aname,np,cost):
#         self.bname=bname
#         self.aname=aname
#         self.np=np
#         self.cost=cost
#     def display(self):
#         print(book.lname,self.bname,self.aname,self.np,self.cost)

# n=int(input())
# i=1
# while(i<=n):
#     bname=input("Enter book name : ")
#     aname=input("Enter author's name : ")
#     np=input("Enter no. of pages : ")
#     cost=input("Enter cost : ")
#     b1=book(bname,aname,np,cost)
#     b1.display()
#     print("*******************************")
#     i+=1


# class employee:
#     org="xyz"
#     def __init__(self,ename,eid,add,salary):
#         self.ename=ename
#         self.eid=eid
#         self.add=add
#         self.salary=salary
#     def display(self):
#         print(employee.org,"||",self.ename,"||",self.eid,"||",self.add,"||",self.salary)
# n=int(input("Enter no. of employees : "))
# for i in range(n):
#     ename=input("Enter Employee name : ")
#     eid=input("Enter Employee id : ")
#     add=input("Enter Employee address : ")
#     salary=int(input("Enter Employee salary : "))
#     e=employee(ename,eid,add,salary)
#     e.display()
#     print("*******************************************")

# STATIC METHODS

# class test:
#     def add(a,b):
#         return a+b
# print(test.add(5,10))

# class triangle:
#     def area(a,b):
#         return (0.5*a*b)
# print(triangle.area(3,2))

# We can use the properties of one class inside another class in two ways
#   1) has a relationship
#   1) in a relationship (inheritance)

# The concept of using the properties of one class into another class by using the class name are reference variable name is know as "has a relationship"

# class x:
#     a=1000
#     def __init__(self):
#         self.b=2000
#     def m1(self):
#         print("in m1 : ")
# class y:
#     c=3000
#     def __init__(self):
#         self.d=4000
#     def m2():
#         print("in m2 : ")
#     def display(self):
#         print(y.c)
#         print(self.d)
#         y.m2()
#         x1=x()
#         print(x1.a)
#         print(x1.b)
#         x1.m1()
# y1=y()
# y1.display()

# class employee:
#     def __init__(self,name,id,sal):
#         self.name=name
#         self.id=id
#         self.sal=sal
#     def display(self):
#         print(self.name,"||",self.id,"||",self.sal)

# class test:
#     def update(e):
#         e.sal=5000
#         e.display()
# e1=employee("Smit","145",100000)
# e1.display()
# test.update(e1)

# class student:
#     def __init__(self, name, rollno, sub1, sub2, sub3):
#         self.name=name
#         self.rollno=rollno
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
#     def display(self):
#         print(self.name, self.rollno, self.sub1, self.sub2, self.sub3)
        
# class findresult:
#     def update(s):
#         s.display()
#         s.total=s.sub1+s.sub2+s.sub3
#         s.avg=s.total/3
#         if(s.sub1>=35 and s.sub2>=35 and s.sub3>=35):
#             print("Pass")
#         else:
#             print("Fail")
            
# s1=student("Raj", 1, 50, 60, 70)
# findresult.update(s1)
# s2=student("Smit", 2, 35, 40, 50)
# findresult.update(s2)

# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         a=3.14*self.r*self.r
#         print("%.2f"%a)
#     def perimeter(self):
#         p=2*3.14*self.r
#         print("%.2f"%p)
# n=int(input())
# a=circle(n)
# a.area()
# a.perimeter()

# INHERITANCE

# The concept of using the properties of one class to another class directly like as a same class number is kmown as inheritance in a relationship
# A class which is extended by another class is known as super class or base class
# A class which is extending another class is known as sub class or derived class
# We can use super class properties into sub class directlt like as same class members

# class x:
#     a=1000
#     def __init__(self):
#         self.b=2000
#     def m1(self):
#         print("in m1:")
# class y(x):
#     c=3000
#     def __init__(self):
#         self.d=4000
#         super().__init__()
#     def m2(self):
#         print("in m2:")
#     def display(self):
#         print(x.a)
#         print(self.b)
#         self.m1()
#         print(y.c)
#         self.m2()
#         print(self.d)
# y1=y()
# y1.display()

# Inheritance is classified into 6 types : 
#     1) Single Inheritance
#     2) Multi-level Inheritance
#     3) Hierchical Inheritance
#     4) Multiple Inheritance
#     5) Cyclic Inheritance
#     6) Hybrid Inheritance

# Single Inheritance :  The concept of inheriting properties from only one class into another class is called Single Inheritance
# Multi-Level Inheritance :  The concept of inheriting properties from multiple classes into a single class is called Multi-Level Inheritance
# Hierchical Inheritance :  The concept of inheriting properties from one class into multiple classes seperately is called Hierchical Inheritance
# Multiple Inheritance :  The concept of inheriting properties from multiple classes into a single class at a time is called Multiple Inheritance
# Cyclic Inheritance :  The concept of inheriting properties from sub class to super class is called Cyclic Inheritance. Python doesn't support it
# Hybrid Inheritance :  The combination of single, multi-level, hierchical and multiple inheritance is called Hybrid Inheritance

# class x:
#     def m1(self):
#         print("in m1:")
# x1=x()
# p=x1.__str__()
# print(p)
# x1.m1()


# Object Class 

# Object class is a pre-defined class defined in build-in module.
# Object is a super class for every class in python.
# Object class properties, we can access in every class directly and we can also acees through, every class reference variable.

# class x:
#     def m1(self):
#         print("in m1")
# class y(x):
#     def m2(self):
#         print("in m2")
# print(x.__bases__)
# print(y.__bases__)
# y1=y()
# y1.m1()
# y1.m2()
# print(y1.__hash__())

# class person:
#     def insert(self):
#         self.name="Krishna"
#         self.add="Hyd"
# class employee(person):
#     def insert1(self):
#         self.id=101
# class salaried_employee(employee):
#     def __init__(self):
#         self.sal=5000
#     def display(self):
#         self.insert()
#         self.insert1()
#         print(self.name,self.add,self.id,self.sal)
# s1=salaried_employee()
# s1.display()

# class student:
#     def insert(self):
#         self.name=input("Enter name")
#         self.id=input("Enter id")
#         self.add=input("Enter address")
# class DS(student):
#     def __init__(self):
#         self.s1=int(input("Enter sub1"))
#         self.s2=int(input("Enter sub2"))
#     def display(self):
#         self.insert()
#         print(self.name,self.id,self.add,self.s1,self.s2)
# class ML(student):
#     def __init__(self):
#         self.s3=int(input("Enter sub1"))
#         self.s4=int(input("Enter sub2"))
#     def display(self):
#         self.insert()
#         print(self.name,self.id,self.add,self.s3,self.s4)
# d1=DS()
# d1.display()
# m1=ML()
# m1.display()

# class x:
#     def m1(self):
#         print("in m1 of x:")
# class y:
#     def m1(self):
#         print("in m1 of y:")
# class z(x,y):
#     def m2(self):
#         print("in m2 of z:")
# z1=z()
# z1.m1()

# class Parent:
#     def add(a,b):
#         print(a+b)
# class Child(Parent):
#     def sub(a,b):
#         print(a-b)
# a=int(input())
# b=int(input())
# Child.add(a,b)
# Child.sub(a,b)


# Polymorphism

# Defining one thing in multiple forms is known as polymorphism.
# Polymorphism is divided into two types :
#     1) Method overloading
#     2) Method overriding

# Method overloading : The concept of defining multiple methods with same name, with same no. of params or diff no. of params within a class is known as method overloading
# It is partially supported by python.

# class x:
#     def m1(self):
#         print("in m1 with no para")
#     def m1(self,a):
#         print("in m1 with one para")
#     def m1(self,a,b):
#         print("in m1 with 2 para")
# x1=x()
# x1.m1(10,20)

# Arbitary Parameter

# If any variable is preceded by start, then the corresponding parameter is called as arbitary parameter.
# Python supports, two types of arbitary parameter.
#     1) single star arbitary parameter is consider as tuple
#     2) Multi star arbitary parameter is consider as dictionary
# 
# def d(*a):
#     print(a)
#     print(sum(a))
#     print(type(a))
# d(10,20,30)

# class test:
#     def op(self,d,*a):
#         self.a=a
#         s=''
#         if d=="str":
#             for i in a:
#                 s=s+i
#             print(s)
#         else:
#             print(sum(a))
# t=test()
# t.op("int",10,20,30)
# t.op("str","Krishna","Ram","Hanuman")

# Method overriding

# The concept of defining multiple methods with same name but with same no. of parameter. One in super class and another in sub class is known as method overriding.
# When we over write super class method with the sub class, then by default sub class method will only executed.

# class x:
#     def m1(self):
#         print("in m1 of x")
#     def m2(self):
#         print("in m2 of x")
# class y(x):
#     def m2(self):
#         print("in m2 of y")
#     def m3(self):
#         print("in m3 of y")
# class z(x):
#     def m1(self):
#         print("in m1 of z")
#     def m4(self):
#         print("in m4 of z")
# y1=y()
# y1.m2()
# y1.m1()
# y1.m3()
# z1=z()
# z1.m2()
# z1.m1()
# z1.m4()

# class x:
#     def m1(self):
#         print("in m1")
#     def __str__(self):
#         return "Python"
# x1=x()
# p=x1.__str__()
# print(p)

# class employee:
#     def __init__(self,name,idl,sal):
#         self.name=name
#         self.idl=idl
#         self.sal=sal
#     def __str__(self):
#         d=self.name+" "+str(self.idl)+" "+str(self.sal)
#         return d
# e1=employee("Krishna",101,80000)
# print(e1)

# Constructor Overriding

# Defining multiple constructors with the same name with same no. of parameters and one constructor is defined in super class and another in sub class is known as Constructor Overriding.
# Whenever we override super class constructor within a sub class, then by default, sub class constructor is executed.

# class x:
#     def __init__(self):
#         print("in constructor of x : ")
# class y(x):
#     def __init__(self):
#         print("in constructor of y : ")
#     def p():
#         return 0
# y1=y()

# class x:
#     def _init_(self,a):
#         print("in constructor of x:", a)
# class y(x):  
#     pass
# y1=y(10)

# class x:
#     def _init_(self, a):
#         self.a=a
#         print(self.a*self.a)
# class y(x):
#     def _init_(self, a,b):
#         self.a=a
#         self.b=b
#         super()._init_(a)
#         print(self.a+self.b)
# y1=y(20)  

# class x:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
# class y(x):
#     def __init__(self, a):
#         self.a=a
#         print(self.a*self.a)
#         super().__init__(10,5)
# y1=y(20)

# class bx:
#     def __init__(self,p):
#         self.p=p
#     def __add__(self,other):
#         d=self.p+other.p
#         return d
# class by:
#     def __init__(self,p):
#         self.p=p
# b1=bx(200)
# b2=by(100)
# c=b1.__add__(b2)
# print(b1+b2)
# print(c)

# class employee:
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
#     def __mul__(self,other):
#         m=self.sal*other.days
#         return m
# class attendance:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
# e1=employee("Krishna",1000)
# a1=attendance("Krishna",10)
# print(e1*a1)

# ABSTRACT CLASSES

# Abstract class is a collection of abstract and non-abstract methods.

# Abstract Method

# The method which does not contain any implementation part, that corressponding method is known as abstract method.

# Non-abstract Method

# The method which contains implementation part, the corresponding methodis known as non-abstract method

# INTERFACE

# Interface is a collection of abstract methods.
# If there is no implementation part for a method or a constructor, we can replace with pass.
# Empty method or constructor is not supported.

# from abc import*
# class RBI(ABC):
#     def min_bal(self):
#         pass
#     def RI(self):
#         print("RI is 6.5%")
# class SBI(RBI):
#     def min_bal(self):
#         print("Min bal is 2000 INR")
# class HDFC(RBI):
#     def min_bal(self):
#         print("Min bal is 0 INR")
# class ICIC(RBI):
#     def min_bal(self):
#         print("Min bal is 500 INR")
# s1=SBI()
# s1.min_bal()
# s2=HDFC()
# s2.min_bal()
# s3=ICIC()
# s3.min_bal()

# from abc import*
# class RBI(ABC):
#   def min_bal(self):
#     pass
#   def RI(self):
#     print("RI is 6,5%")
# class SBI(RBI):
#   def min_bal(self):
#     print("Min-bal is 2000 rupess:")
# class HDFC(RBI):
#   def min_bal(self):
#     print("Min-bal is 0 rupess:")
# class ICIC(RBI):
#   def min_bal(self):
#     print("Min-bal is 500 rupess:")

# s = input("enter class name:")   # it will take the class name and according to that it will exceute , because it don't know about card , so we make them to choose the card.
# c = globals()[s]     # it will convert the correspoing string into their respective class string
# c1=c()
# c1.min_bal()
# c1.RI()

# from abc import*
# class car(ABC):
#     def __init__(self,regno):
#         self.regno=regno
#     def opentank(self):
#         print("Fill in tank with reg no. : ",self.regno)
#     def steering(self):
#         pass
#     def breaking(self):
#         pass
# class porsche(car):
#     def steering(self):
#         print("Manual Steering")
#     def breaking(self):
#         print("Hydraulic Brakes")

# p1=porsche("SP1324")
# p1.opentank()
# p1.steering()
# p1.breaking()

# INTERFACE

# It is a collection of abstract methods.
# It is implemented by inheriting the properties of abc module.

# from abc import *
# class test(ABC):
#     def operation(slef):
#         pass
# class sub1(test):
#     def operation(self,a):
#         print(a*a)
# class sub2(test):
#     def operation(self,a):
#         print(a**3)
# class sub3(test):
#     def operation(self,a):
#         print(a+a)
# s1=sub1()
# s1.operation(10)
# s2=sub2()
# s2.operation(10)
# s3=sub3()
# s3.operation(10)

# from abc import *
# class vehicle:
#     def __init__(self,regno):
#         self.regno=regno
#     def DisplayNo(self):
#         print("Youa re viewing the vehicle of no. : ",self.regno)
#     def NoOfTires(self):
#         pass
# class bike(vehicle):
#     def NoOfTires(self,a):
#         print("No. of wheels : ",a)
# class rikshaw(vehicle):
#     def NoOfTires(self,a):
#         print("No. of wheels : ",a)
# class car(vehicle):
#     def NoOfTires(self,a):
#         print("No. of wheels : ",a)
# b1=bike("SP1324")
# b1.DisplayNo()
# b1.NoOfTires(2)
# r1=rikshaw("SP2004")
# r1.DisplayNo()
# r1.NoOfTires(3)
# c1=car("SP1234")
# c1.DisplayNo()
# c1.NoOfTires(4)

# ACCESS MODIFIERS IN PYTHON

# In python, we have three access modifiers;
#     1) Public
#     2) Private
#     3) Protected

# Public : If variable or method is public, we can access anywhere within the program. 
# Protected : If variable or method is protected, we can access within the next immediate class (we can't acess in the main program). 
# Private : If variable or method is private, we can only access within the same class.

# class employee:
#     def __init__(self,name,idl,sal,dep):
#         self.name=name
#         self.idl=idl
#         self.sal=sal
#         self.dep=dep
#     def display(self):
#         print(self.name,self.idl,self.sal,self.dep)
# e1=employee("Smit",145,100000,"Web-Dev")
# e1.display()

# Protected variable can be declared using _

# class employee:
#     def __init__(self,name,idl,sal,dep):
#         self._name=name
#         self._idl=idl
#         self._sal=sal
#         self._dep=dep
#     def _display(self):
#         print("Name :",self._name)
#         print("Id :",self._idl)
# class geeks(employee):
#     # def __init__(self,name,idl,sal,dep):
#     #     super().__init__(name,idl,sal,dep)
#     def display(self):
#         self._display()
#         print("Salary :",self._sal)
#         print("Department :",self._dep)

# e1=geeks("Smit",145,100000,"Web-Dev")
# e1.display()

# Private Variable : In python programming, we can declare a private variable and private methods using __

# class employee:
#     def __init__(self,name,idl,sal,dep):
#         self.__name=name
#         self.__idl=idl
#         self.__sal=sal
#         self.__dep=dep
#     def __display(self):
#         print("Name :",self.__name)
#         print("Id :",self.__idl)
#         print("Salary :",self.__sal)
#         print("Department :",self.__dep)
#     def display(self):
#         self.__display()
# # class geeks(employee):
# #     # def __init__(self,name,idl,sal,dep):
# #     #     super().__init__(name,idl,sal,dep)
# #     def display(self):
# #         self.__display()

# e1=employee("Smit",145,100000,"Web-Dev")
# e1.display()

#---------------------------------------------------BREAK--------------------------------------------------------#---------------------------------------------------BREAK--------------------------------------------------------


# def append_numbers(start, end, result=[]):
#     if start >= end:
#         result.append(start)
#         append_numbers(start - 1, end, result)
#     return result

# numbers_list = append_numbers(5, 1)
# print(numbers_list)

# def append_numbers(start, end, result=[]):
#     if start <= end:
#         result.append(start)
#         append_numbers(start + 1, end, result)
#     return result

# numbers_list = append_numbers(1, 5)
# print(numbers_list)
