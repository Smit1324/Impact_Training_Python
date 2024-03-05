# def catalan(n):
#     if (n==0 or n==1):
#         return 1
#     catalan = [0]*(n+1)
#     catalan[0] = 1
#     catalan[1] = 1
#     for i in range(2, n+1):
#         for j in range(i):
#             catalan[i] += catalan[j] * catalan[i-j-1]
#     return catalan[n]

# for i in range(5):
#     print(catalan(i),end=" ")

# # [0,0,0,0]
# #  0 1 2 3
# # j=0,1,
# # catalan[2]=catalan[2]+1*1
# # catalan[2]=0+1=1
# # j=1
# # catalan[2]=1+1*1=1+1=2

# # catalan[3]=2+catalan[1]*catalan[1]=2+1
# # catalan[3]=3+catalan[2]*catalan[0]=3+2*1=5

# # for i in range(2,n+1):
# #     for j in range(i):
# #         catalan[i]+=catalan[j]*catalan[i-j-1]

# # n=3
# # j=2,3
# # i=2
# # j=0,1
# # i=3
# # j=0,1,2
# # catalan[3]=catalan[3]+catalan[0]*catalan[2]=0+1*2=2

# # catalan[4]=catalan[4]+catalan[0]*catalan[3]=0+1*5=5
# # catalan[4]=catalan[4]+catalan[1]*catalan[2]=5+1*2=7
# # catalan[4]=catalan[4]+catalan[2]*catalan[1]=7+2*1=9
# # catalan[4]=catalan[4]+catalan[3]*catalan[0]=9+5*1=14
# # catalan[4]=14


n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(1,n+1)
    if i not in l:
        print(i)