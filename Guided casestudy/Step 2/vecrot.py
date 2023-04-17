import math
from matplotlib import pyplot as plt
import numpy as np

#Define the vector
X=[[5],[0]]

#Specify the angle with which you want to rotate
a=math.pi

#Rotation matrix
T=[[math.cos(a),math.sin(a)],
  [-math.sin(a),math.cos(a)]]

#Resultant Matrix
Y=[[0],[0]]

for i in range(len(T)):
    for j in range(len(X[0])):
        for k in range(len(X)):
            Y[i][j]+=T[i][k]*X[k][j]  # type: ignore
        
print(Y)
Z=np.array([X,Y])
origin = np.array([[0, 0], [0, 0]])
plt.quiver(*origin, Z[:, 0], Z[:, 1],color=['black', 'red'],scale = 20)
plt.show()