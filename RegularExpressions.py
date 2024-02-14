# REGULAR EXORESSION

# If you want to representa group of strings according to particular format or pattern, then we should go for regular expression.
# Regular expression is a declarative mechanism to represent a group of strings according to particular pattern.
# Example1 We can write a RE to represent the mobile number of 10 digits.
# Example2: We can write a RE to represent the email id.
# The main important application areas of regular expression are:
# 1. To develop validation frameworks.
# 2. To develop pattern matching application.
#     Ex1 : ctrl + f in windows and grep in unix
# 3.To develop translators like compilers, interpreters etc.
# 4. To develop digital circuits.

# We can develop regular expression based applications by using the following modules : re
# This module contains several inbuild functions to work with regular expression very easily :
# compile() : To compile regular expression
# finditer() : Returns an iterative object which yields match object for every match
# An match object, we can call the following methods:
#     start()
#     end()
#     group()

# import re
# c=0
# p=re.finditer("ab","abaabbab")
# for s in p:
#     c+=1
#     print(s.start(),"...",s.end(),"...",s.group())
# print("The number of occurences:",c)

# IMPORTANT FUNCTIONS OF re MODULE

# 1. match() : To check the given pattern at the beginning of the target string.
# 2. fullmatch() : To check the given pattern is completely available in the target string or not.
# 3. search() : To search the given pattern in the target string.
# 4. findall() : To return all occurences of the pattern from the target string.
# 5. finditer() : To return all occurences of the pattern from the target string as an iterative object.
# 6. sub() : To replace the occurences of the pattern with specified string.
# 7. subn() : To return the number of replacements.
# 8. split() : To split the target string based on the given pattern.

# 1. match() function
# import re
# p=re.match("in","india")
# if p!=None:
#     print("Match is available at the beginning of the string")
#     print(p.start(),"...",p.end(),"...",p.group())
# else:
#     print("Match is not available at the beginning of the string")

# 2. fullmatch() function
# import re
# p=re.fullmatch("india","india")
# if p!=None:
#     print("Full string is matched")
# else:
#     print("Full string is not matched")

# 3. search() function
# import re
# p=re.search("india","india is my country")
# if p!=None:
#     print("Match is available at the beginning of the string")
#     print(p.start(),"...",p.end(),"...",p.group())
# else:
#     print("Match is not available at the beginning of the string")

# 4. findall() function
# import re
# p=re.findall("[a-z]","abaabbab")
# print(p)

# 5. finditer() function
# import re
# p=re.finditer("[a-z]","a1b2igh3")
# for i in p:
#     print(i.start(),"...",i.end(),"...",i.group())

# 6. sub() function
# import re
# p=re.sub("[0-9]","*","a1b2igh3")
# print(p)

# 7. subn() function
# import re
# p=re.subn("[0-9]","*","a1b2igh3")
# print(p)

# ^ SYMBOL

# ^ symbol is used to check whether the given pattern is available at the beginning of the target string or not.
# If the target string starts with a given pattern, then it return match objects otherwise it returns None.

# import re
# l=re.search("^learning","learning python is very easy") 
# if l!=None:
#     print("The target string starts with the given pattern")
# else:
#     print("The target string does not start with the given pattern")

# $ SYMBOL

# $ symbol is used to check whether the given pattern is available at the end of the target string or not.
# If the target string ends with a given pattern, then it return match objects otherwise it returns None.

# import re
# l=re.search("easy$","learning python is very easy")
# if l!=None:
#     print("The target string ends with the given pattern")
# else:
#     print("The target string does not end with the given pattern")

# import re
# l=re.finditer("[abc]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[^abc]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[a-z]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[^a-z]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[0-9]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[^0-9]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[a-zA-Z]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[a-z0-9A-Z]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("[^a-z0-9A-Z]","a7b@K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# Pre defined Character classes:
# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .  Any character including special characters

# import re
# l=re.finditer("\s","a7b @K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("\S","a7b @K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# import re
# l=re.finditer("\D","a7b @K9z")
# for p in l:
#     print(p.start(),"...",p.group())

# WAP to check the given mobile number is valid or not.
# import re
# n=input("Enter mobile number:")
# x="[6-9][0-9]{9}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

# WAP to check the given number plate is valid or not.
# import re
# n=input("Enter number plate:")
# v=re.fullmatch("[A-Z]{2}\s\d{4}",n)
# if v is not None:
#     print("Valid")
# else:
#     print("Invalid")

# WAP to check the given email id is valid or not.
# import re
# n=input("Enter email id:")
# v=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",n)