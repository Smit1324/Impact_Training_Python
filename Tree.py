# TREE

# Organizing data in hierchical form, in non linear form.
# Organizing the data in hierchical fashion without any closed path.
# Tree is a collection of nodes and nodes contains the elements.
# Nodes will be connected by edges.

# BASIC TERMINOLOGIES OF TREE

# Node : It is an element of the tree.
# A tree have number of nodes.

# Root Node : It is the top most node of the tree (where branch occurs).
# Tree will have only one root node.
# Edge : A link between one node to another node or connection b/w the nodes.
# If we have n nodes then we will have n-1 edges.

# Parent Node : The node which is connected to the child node (has branches).

# Child Node : The node which is connected to the parent node (branches of a parent).
# Node with edge from bottom to top is child node.
# Siblings : Childres of a same parent.

# Leaf Node : The node which does not have any child node.

# Internal Node : The node which has atleast one child node i.e., all the nodes other than the leaf node.

# Degree of a Tree : The number of child node will represent the degree of a tree.
# Maximum degree of all nodes is called degree of a tree or node with maximum no.of children.

# LEVEL OF A TREE

# Each step or hierchical of a tree is called level of a tree.

# HEIGHT OF A TREE

# The longest path from root node to leaf node is called height of a tree.

# DEPTH OF A TREE

# The longest path from root node to a particular node is called depth of a tree.


# Node with children form a subtree.


# BINARY TREE

# A tree with nodes having atmost two children is called binary tree.


# CONSTRUCTION OF BINARY TREE 

# If the tree is empty then create a root node and insert the element.
# If the element is greater than the root node, insert a right sub tree.
# If the element is less than the root node, insert a left sub tree.

# TRAVERSAL TECHNIQUES OF A TREE

# 1. Preorder Traversal
# 2. Postorder Traversal
# 3. Inorder Traversal

# Postorder Traversal : Left, Right, Root
# Preorder Traversal : Root, Left, Right
# Inorder Traversal : Left, Root, Right

# WAP to construct a binary tree and print the binary tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = Node(data)
#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.data, end=" ")
#         if self.right:
#             self.right.print_tree()
#     def preorder(self):
#         print(self.data,end=" ")
#         if self.left:
#             self.left.preorder()
#         if self.right:
#             self.right.preorder()
#     def postorder(self):
#         if self.left:
#             self.left.postorder()
#         if self.right:
#             self.right.postorder()
#         print(self.data,end=" ")
#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.data,end=" ")
#         if self.right:
#             self.right.inorder()
# b=Node(10)
# b.insert(14)
# b.insert(35)
# b.insert(10)
# b.insert(19)
# b.insert(31)
# b.insert(35)
# # b.print_tree()
# # b.preorder()
# # b.postorder()
# # b.inorder()

