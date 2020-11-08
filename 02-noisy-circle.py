import numpy as np
import matplotlib.pyplot as plt

xy=np.loadtxt(open("data/noisy-circle.csv", "rb"), delimiter=",", skiprows=1)

x_vals=xy[:,0]
y_vals=xy[:,1]

def estimate_circle(x,y):
    # F(X) = ( x - cx ) ^ 2 + ( y - cy ) ^ 2 - r^2

    # X0 estimation
    X = np.array([0.0,0.0,1.0])

    # F(X0) + dX * F'(X0) = 0
    # dF(X) / dcx = - 2 * ( x - cx )
    # dF(X) / dcy = - 2 * ( y - cy )
    # dF(X) / dr  = - 2 * r
    for k in range(100):
        FX0 = np.zeros(x.size)
        A   = np.zeros((x.size,3))
        for i in range(x.size):
            FX0[i] = ( x[i] - X[0] )**2 + ( y[i] - X[1] )**2 - X[2]**2
            A[i,0] = - 2 * ( x[i] - X[0] )
            A[i,1] = - 2 * ( y[i] - X[1] )
            A[i,2] = - 2 * X[2]

        dX, residual = np.linalg.lstsq(A,-FX0,rcond=None)[:2]
        X = X + dX
        print(X)
    return X

X = estimate_circle(x_vals,y_vals)

plt.plot(x_vals, y_vals, 'r+', label='data')
plt.xlabel('x')
plt.ylabel('y')
circle = plt.Circle((X[0], X[1]), X[2], color='b', fill=False)
plt.gcf().gca().add_artist(circle)
plt.show()
