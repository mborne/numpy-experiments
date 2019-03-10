import numpy as np
import matplotlib.pyplot as plt

xy=np.loadtxt(open("data/noisy-line.csv", "rb"), delimiter=",", skiprows=1)

x=xy[:,0]
y=xy[:,1]

#print(x)
#print(y)

# a * x + b = y
A = np.column_stack((x,np.ones(x.size)))

# least square solve A*X = y
X, residual = np.linalg.lstsq(A,y,rcond=None)[:2]
print("y = %.5f . x + %.5f " % (X[0],X[1]) )

ySol= X[0] * x + X[1]

plt.plot(x,y, label='data')
plt.plot(x,ySol, label='model')

plt.xlabel('x')
plt.ylabel('y')
plt.show()


