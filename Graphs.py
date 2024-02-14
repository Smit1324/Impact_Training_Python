# GRAPH

# Graph is a collection of vertices and edges.
# Vertices will be represented by circle or nodes or holes.
# Edges will represented the line.
# Edges will connect the line.

# Tree
#                                     (A)                             
#                                     / \
#                                     (B) (C)

# Graph
#                                     (A)
#                                     / \
#                                 (B)----(C)


# Degree of a node:
#     The number of edges connected to each node.

# CYCLIC GRAPH

# Cyclic Graph will represent the total no. of adjacent nodes.

# DIFFERENT TYPES OF GRAPH

# 1. Directed Graph : In this graph, the edges will be represented by the arrow.
# 2. Undirected Graph : In this graph, the edges will be represented by the line. (no direction)
# 3. Weighted Graph : In this graph, the edges will be represented by the weight.
# 4. Unweighted Graph : In this graph, the edges will be represented by the no weight.
# 5. Cyclic Graph : If the graph is forming a circle, then it is called as cyclic graph.
# 6. Acyclic Graph/Uncyclic Graph : If the graph is not forming a circle, then it is called as acyclic graph.

# GRAPH REPRESENTATION

#1. Using multidimensional array
#2. Using a list

# TRAVERSAL TECHNIQUES IN GRAPH

#1. Breadth First Search (BFS)
#2. Depth First Search (DFS)

# BFS : It is similar to implementation of the queue.
# DFS : It is similar to implementation of the stack.

# Queue works on the principle of FIFO (First In First Out)
# Stack works on the principle of LIFO (Last In First Out)


# -------------------------------------------------------------BREAK---------------------------------------------
# -------------------------------------------------------------BREAK---------------------------------------------

# WAP to read a string from the user and check wether it is compressive string or not.

# s=input()
# l=len(s)
# d={p:s.count(p) for p in s}
# news=""
# for i,j in d.items():
#     news=news+i+str(j)
# print(news)
# if len(news)<l:
#     print("YES")
# else:
#     print("NO") 