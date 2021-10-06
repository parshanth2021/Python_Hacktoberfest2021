import numpy as np
# Algorithm
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    print('dist before loops',dist)
    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    print('dist after loops',dist)
    sol(dist)

# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                answer[p][q]=dist[p][q]
                print("INF", end=" ")
            else:
                answer[p,q]=dist[p][q]
                print(dist[p][q], end="  ")
        print(" ")

'''rows=int(input('rows'))
columns=int(input('columns'))'''
c,f=input('enter c and f :').split()
c=int(c)
nV=c
INF=999
matrix=np.full((c,c),INF)
(np.fill_diagonal(matrix,0))
print(matrix)
f=int(f)
for i in range(f):
    i,j,k=input('enter value if i,j,k :').split()
    i=int(i)
    j=int(j)
    k=int(k)
    matrix[i-1,j-1]=k
    matrix[j-1,i-1]=matrix[i-1,j-1]
print(matrix)
answer=np.full((nV,nV),0)
G=floyd(matrix)
print('answer matrix is ',answer)
