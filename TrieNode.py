# class TrieNode:
#   def _init_(self):
#     self.children = {}
#     self.is_end_of_word = False
# class Trie:
#   def _init_(self):
#     self.root = TrieNode()

#   def insert(self, word):
#     node = self.root
#     for char in word:
#       if char not in node.children:
#         node.children[char] = TrieNode()
#       node = node.children[char]
#     print(node.children)
#     node.is_end_of_word = True
#   def search(self, word):
#     node = self.root
#     for char in word:
#       if char not in node.children:
#         return False
#       node = node.children[char]
#     return node.is_end_of_word

#   def starts_with(self, prefix):
#     node = self.root
#     for char in prefix:
#       if char not in node.children:
#         return False
#       node = node.children[char]
#     return True
# # Example usage:
# trie = Trie()
# words = ["apple", "app", "banana", "bat","ball"]
# for word in words:
#   trie.insert(word)

# print(trie.search("apple"))  #output: True
# print(trie.search("app"))  #output: True
# print(trie.search("banana"))  #output: True
# print(trie.search("bat"))  #output: True
# print(trie.search("ball"))  #output: True
# print(trie.search("orange"))  #output: False

# print(trie.starts_with("app"))  #output: True
# print(trie.starts_with("ban"))  #output: True
# print(trie.starts_with("bal"))  #output: True


# s=[[1,2,3],[4,5,6],[7,8,9]]
# output [[9,8,7],[6,5,4],[3,2,1]]
# s.reverse()
# for i in s:
#     i.reverse()
# print(s)
# d=[]
# for i in s[::-1]:
#     r=i[::-1]
#     d.append(r)
# print(d)
# g=[p[::-1] for p in s[::-1]]
# print(g)

# l=list(map(int,input().split()))
# print(l)
# if len(l)%2==0:
#     m=l[len(l)//2]+l[(len(l)-1)//2]
#     l.remove(l[len(l)//2])
#     l.remove(l[len(l)//2])
#     o=len(l)//2
#     l.insert(o,m)
#     print(l)
# else:
#     print(l)

# n=int(input())
# l=list(map(int,input().split()))[:n]
# c=int(input())
# s=sum(l)
# if sum(l)<c:
#     r=s//c
# else:
#     r=(s//c)+1
# print(r)
