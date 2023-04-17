
import matplotlib.pyplot as plt
import numpy as np
#Define the vector
X=[[2],[0]]
   
#Specify the rotation angle
a=np.pi/3
   
#Rotation matrix
T=[[np.cos(a),np.sin(a)],
  [-np.sin(a),np.cos(a)]]
   
#Rotated vector
Y=[[0],[0]]
   
for i in range(len(T)):
    for j in range(len(X[0])):
        for k in range(len(X)):
            Y[i][j]+=T[i][k]*X[k][j]  # type: ignore

#Now we need to reflect this vector Y along y=x line
   
Z=[[0],[0]]
   
#Reflection along y=x matrix
R=[[0,1],
  [1,0]]
   
for i in range(len(R)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            Z[i][j]+=R[i][k]*Y[k][j]
print(Z)    
P=np.array([X,Z])
origin = np.array([[0, 0], [0, 0]])
plt.quiver(*origin,P[:,0],P[:,1],color=['black','red'], scale = 8)
plt.show()