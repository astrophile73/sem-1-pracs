from re import I
import numpy as np
import math
## Forming Hilbert matrix of order 10x10
s = 10
H = np.zeros((s, s))
for c in range(s):
    for r in range(s):
        H[c, r] = 1 / (c + r + 1)
n = len(H)     
## Inverse of Hilbert Matrix
I = np.array([[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,1]],dtype='float')
A=np.concatenate((H,I),axis=1)
n=len(A)
def pivot(k):  # type: ignore
    for i in range (k+1,n):
        if abs(A[i,k])>abs(A[k,k]):
            A[[k,i]]=A[[i,k]]
            return
# Gauss eleimination steps
for k in range (n-1):
    if abs(A[k,k])<1.0e-06:
       pivot(k)
    for i in range (k+1,n):
       ratio=A[i,k]/A[k,k]
       A[i,:]=A[i,:]-ratio*A[k,:]
B=A[:, 0:10]
D=A[:,10:20]
F=np.concatenate((B,D),axis=1)     
m=len(F)
def pivot(k):
   for i in range (k+1,m):
       if abs(F[i,k])>abs(F[k,k]):
           F[[k,i]]=F[[i,k]]
           return
# Gauss eleimination steps
for k in range (m-1):
    if abs(F[k,k])<1.0e-06:
        pivot(k)
    for i in range (k+1,m):
        ratio=F[i,k]/F[k,k]
        F[i,:]=F[i,:]-ratio*F[k,:]
J=F[:,10:20]
print('\nThe inverse matrix is:\n',J)
result=np.zeros((10,10))
for i in range (len(J)):
    for j in range(len(H[0])):
        for k in range(len(H)):
            result[i][j]+=J[i][k]*H[k][j]
print('\nThe resultant of the multiplication is:\n',result)        