# DATA STRUCTURES:-
# -----------------

# --> Performing manupulation on data is called as data structures.
# -- > Different manupulation on data are:-

# 1) Storing the data 
# 2) Updating the data 
# 3) Retriving the data
# 4) Deleting the data


# --> Various data structure concept are:-

# 1) Stack
# 2) Queue
# 3) Searching ans Sorting technique
# 4) Linkedlist
# 5) Trees
# 6) Graph

# # lINKED LIST:-
#   --------------

# -> It is a collection of nodes and everynode will be connected to the next node .

# ==> It is clasified into three types.

# 1) Single Linked list
# 2) Double Linked list
# 3) Circular Linked list


# # Single Linkedlist:-
# ---------------------

# ---> it is a collection of nodes and everynode will contain two fields 
# 1) data 
# 2) next

# ---> The various operations we are going to perform such as :-
# 1) Creating the node
# 2) Inserting the data into the node
# 3) Displaying the data present in the node
# 4) Adding the node
# 5) Deleting the node
# 6) Displaying the data in the reverse order.

# Single Linkedlist Rough code :-
# def display(self):
#     if(self.head==None):
#         print("Linked list is empty")
#     else:
#         temp=self.head
#         while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next    


# Code for single linkedlist:-        
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.display()

# wap to reverse the linked list:-

# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
#     def rdisplay(self):
#         l=[]
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#             while(temp):
#                 d=temp.data
#                 l.append(d)
#                 temp=temp.next
#         for i in range(len(l)-1,-1,-1):
#             print(l[i],end="-->") 
        
        
# n1=Node(10)        
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4      
# s1.rdisplay()  
      
# wap to add the node at the begining of the linked list:-

# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_beg(self,data):
#         nb=Node(data)
#         temp=self.head
#         nb.next=temp    
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_beg(5)
# s1.display()

# wap to add the node at the end of the linked list:-

# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_end(self,data):
#         ne=Node(data)
#         temp=self.head
#         while(temp.next!=None):
#             temp=temp.next
#         temp.next=ne
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_end(50)
# s1.display()

# wap to add the node at the specific position of the linked list:-

# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
        
# wap to add the node at the specific position of the linked list:-

# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_pos(self,data,pos):
#         np=Node(data)
#         temp=self.head
#         for i in range(1,pos):
#             temp=temp.next
#         np.next=temp.next
#         temp.next=np
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_pos(25,2)
# s1.display()

# wap to delete first node:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_del(self):
#         temp=self.head
#         self.head=temp.next
#         temp.next=None
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_del()
# s1.display()

# wap to delete the last node:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_del(self):
#         temp=self.head
#         while(temp.next.next!=None):
#             temp=temp.next
#         temp.next=None
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_del()
# s1.display()

# wap to delete the node at the specific position:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.next=None
# class slinkedlist:
#     def _init_(self):
#         self.head=None
#     def node_del(self,pos):
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         temp.next=temp.next.next
#     def display(self):
#         temp=self.head
#         if(self.head==None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="-->")
#             temp=temp.next
# n1=Node(10)
# s1=slinkedlist()
# s1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# s1.node_del(2)
# s1.display()

# double linked list:-
# double linked list is a collection of nodes and every node will be connected with the next node.
# in double linked list every node will contain three fields.
# 1) prev(previous node address)
# 2) data
# 3) next(next node address)
# for the 1st node prev node address will be null. 
# for the last node next field address will be null. 
# the basic opetrations we can perform on the double linked list are:-
# 1) creating the nodes
# 2) inserting the data into the nodes.
# 3) displaying the data present in the nodes.
# 4) reversing the data present in the nodes through the tail.
# 5) adding the node
# 6) deleting the node

# Logic for double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
# d1=dlinkedlist()
# n1=Node(10)
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4   

# code for double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#         temp=self.head
#         if(self.head is None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="<-->")
#             temp=temp.next
# n1=Node(10)
# d1=dlinkedlist()
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4
# d1.display()   

# wap to reverse the double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
#     def rdisplay(self):
#         temp=self.tail
#         if(self.tail is None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="<-->")
#             temp=temp.prev
# n1=Node(10)
# d1=dlinkedlist()
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4
# d1.rdisplay()         
         
# wap to add the node at the begining of the double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
#     def node_beg(self,data):
#         nb=Node(data)
#         temp=self.head
#         nb.next=temp
#         temp.prev=nb
#         self.head=nb
#     def display(self):
#         temp=self.head
#         if(self.head is None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="<-->")
#             temp=temp.next
# n1=Node(10)
# d1=dlinkedlist()
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4
# d1.node_beg(5)
# d1.display()

# wap to add the node at the end of the double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
#     def node_end(self,data):
#         ne=Node(data)
#         temp=self.head
#         while(temp.next!=None):
#             temp=temp.next
#         temp.next=ne
#         ne.prev=temp
#     def display(self):
#         temp=self.head
#         if(self.head is None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="<-->")
#             temp=temp.next
# n1=Node(10)
# d1=dlinkedlist()
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4
# d1.node_end(50)
# d1.display()

# wap to add the node at the specific position of the double linked list:-
# class Node:
#     def _init_(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinkedlist:
#     def _init_(self):
#         self.head=None
#         self.tail=None
#     def node_pos(self,data,pos):
#         np=Node(data)
#         temp=self.head
#         for i in range(1,pos):
#             temp=temp.next
#         np.next=temp.next
#         temp.next.prev=np
#         np.prev=temp
#         temp.next=np
#     def display(self):
#         temp=self.head
#         if(self.head is None):
#             print("Linked list is empty")
#         else:
#          while(temp):
#             print(temp.data,end="<-->")
#             temp=temp.next
# n1=Node(10)
# d1=dlinkedlist()
# d1.head=n1
# n2=Node(20)
# n1.next=n2
# n2.prev=n1
# n3=Node(30)
# n2.next=n3
# n3.prev=n2
# n4=Node(40)
# n3.next=n4
# n4.prev=n3
# d1.tail=n4
# d1.node_pos(25,2)
#  d1.display()


# CIRCULAR LINKED LIST

# Circular linked list is similar to single linked list but in a singel linked list, the last node address will be null, however in the circular linked list, last node will be connected to first node, that's why last node address is address of first node.
# Single linked list contains only head but circular linked list contains both head and tail.
# Head always pointing to first node.
# Tail always pointing to last node

# [L1|A1(address of L2)]-->[L2|A1(address of L3)]-->[L3|A1(address of L4)]-->[L4|A1(address of L1)]

# WAP to create 4 nodes in a circular linked list and display the data present in the linked list and reverse the data present in the nodes.

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class cll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#         if(self.head is None):
#             print("EMPTY")
#         else:
#             temp=self.head
#             while(True):
#                 print(temp.data,end="--->")
#                 temp=temp.next
#                 if(temp==self.head):
#                     break
#             print(temp.data)

# l1=cll()
# n1=Node(10)
# l1.head=n1
# l1.tail=n1
# l1.tail.next=l1.head
# n2=Node(20)
# l1.tail.next=n2
# l1.tail=n2
# l1.tail.next=l1.head
# n3=Node(30)
# l1.tail.next=n3
# l1.tail=n3
# l1.tail.next=l1.head
# n4=Node(40)
# l1.tail.next=n4
# l1.tail=n4
# l1.tail.next=l1.head
# l1.display()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class cll:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def display(self):
#         if(self.head is None):
#             print("EMPTY")
#         else:
#             temp=self.head
#             while(True):
#                 print(temp.data,end="--->")
#                 temp=temp.next
#                 if(temp==self.head):
#                     break
#             print(temp.data)
#     def node_beg(self,data):
#         temp=self.head
#         nb=Node(data)
#         self.head=nb
#         nb.next=temp
#         self.tail.next=nb
#     def node_end(self,data):
#         temp=self.head
#         ne=Node(data)
#         self.tail.next=ne
#         self.tail=ne
#         self.tail.next=temp
#     def node_pos(self,data,pos):
#         np=Node(data)
#         temp=self.head
#         for i in range(1,pos):
#             temp=temp.next
#         np.next=temp.next
#         temp.next=np
#     def rdisplay(self):
#         prev=self.tail
#         curr=self.head
#         while(True):
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#             if (curr==self.head):
#                 break
#         self.tail=self.head
#         self.head=prev 
#     def del_beg(self):
#         temp=self.head
#         self.head=temp.next
#         self.tail.next=self.head
#     def del_end(self):
#         temp=self.head
#         while(temp.next.next!=self.head):
#             temp=temp.next
#         temp.next=self.head
#         self.tail=temp
#     def del_pos(self,pos):
#         temp=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#         temp.next=temp.next.next

# l1=cll()
# n1=Node(10)
# l1.head=n1
# l1.tail=n1
# l1.tail.next=l1.head
# n2=Node(20)
# l1.tail.next=n2
# l1.tail=n2
# l1.tail.next=l1.head
# n3=Node(30)
# l1.tail.next=n3
# l1.tail=n3
# l1.tail.next=l1.head
# n4=Node(40)
# l1.tail.next=n4
# l1.tail=n4
# l1.tail.next=l1.head
# # l1.rdisplay()
# # l1.node_beg(50)
# # l1.node_end(50)
# # l1.node_pos(60,2)
# # l1.del_beg()
# # l1.del_end()
# # l1.del_pos(3)
# l1.display()


# -------------------------------------------------------------BREAK---------------------------------------------
# -------------------------------------------------------------BREAK---------------------------------------------

# n=int(input("Enter no. of inputs in dictionary"))
# d={}
# for p in range(n):
#     k=input("Enter key : ")
#     v=int(input("Enter value : "))
#     d[k]=v
# val=int(input("Enter a value whoes key you need : "))
# keys=[]
# for i,j in d.items():
#     if val==j:
#         print(i, end=" ")
#         break


# -------------------------------------------------------------BREAK---------------------------------------------
# -------------------------------------------------------------BREAK---------------------------------------------

