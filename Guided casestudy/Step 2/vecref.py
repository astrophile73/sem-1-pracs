import numpy as np
import matplotlib.pyplot as plt


#Define the vector

X=[[0],[1]]

#Reflection matrix
T=[[0,1],
  [1,0]]

#Result matrix
Y=[[0],[0]]

for i in range(len(T)):
    for j in range(len(X[0])):
        for k in range(len(X)):
            Y[i][j]+=T[i][k]*X[k][j]
        
print(Y)
Z=np.array([X,Y])
origin = np.array([[0, 0], [0, 0]])
plt.quiver(*origin, Z[:, 0], Z[:, 1],color=['black', 'red'],scale=5)
plt.xlim([-0.01,0.01])

plt.show()