# Priority Queue

# -> Priority Queue is similar to queue operation. 
# -> In priority queue we can assign the priority according to the priority elements gets deleted.
# -> Different ways of priority queue:-

# 1) Ascending order
# 2) Descending order

# class pq:
#   def _init_(self):
#     self.queue=[]
#   def push(self,x):
#     self.queue.append(x)
#   def display(self):
#     print(self.queue)
#   def delete(self):
#     self.queue.sort() #[1,2,5,7,8]
#     print("Deleted element is:", self.queue.pop(0))

# p1=pq()
# p1.push(7)
# p1.push(2)
# p1.push(1)
# p1.push(8)
# p1.push(5)
# p1.display()
# p1.delete()
# p1.delete()
# p1.display()

# wap to reverse an element prsent in the stack
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,element):
#         self.stack.append(element)
#     def pop(self):
#         return self.stack.pop()
#     def reverse(self):
#         self.stack = self.stack[::-1]
#     def display(self):
#         print(self.stack)
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50)
# s.display()
# s.reverse()
# s.display()

## Wap to reverse a string using stack approach using pop and push method and also object orientd programming
# class Stack:
#     def _init_(self):
#         self.stack = []

#     def push(self, element):
#         self.stack.append(element)

#     def pop(self):
#         if len(self.stack) <= 0:
#             print("Stack is Empty")
#         else:
#             return self.stack.pop()

#     def display(self):
#         print(self.stack)

#     def reverse(self, str):
#         for i in str:
#             self.push(i)
#         rev_str = ""
#         while len(self.stack) > 0:
#             rev_str += self.pop()
#         return rev_str

# s = Stack()
# input_str = "Anjali"
# print("Original string: ", input_str)
# print("Reversed string: ", s.reverse(input_str))

# n1,n2,n3=map(int,input().split())
# stack1=list(map(int,input().split()))
# stack2=list(map(int,input().split()))
# stack3=list(map(int,input().split()))

# sum1,sum2,sum3=sum(stack1),sum(stack2),sum(stack3)

# while sum1!=sum2 or sum2!=sum3:
#     if sum1>=sum2 and sum1>=sum3:
#         sum1-=stack1.pop(0)
#     elif sum2>=sum1 and sum2>=sum3:
#         sum2-=stack2.pop(0)
#     elif sum3>=sum1 and sum3>=sum2:
#         sum3-=stack3.pop(0)
# print(sum1)