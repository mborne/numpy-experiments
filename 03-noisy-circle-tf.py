# inspired from https://stackoverflow.com/a/57760158

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# load noisy circle data
xy=np.loadtxt(open("data/noisy-circle.csv", "rb"), delimiter=",", skiprows=1)
x_vals=xy[:,0]
y_vals=xy[:,1]

# Setup a stochastic gradient descent optimizer
opt = tf.keras.optimizers.SGD(learning_rate=0.0001)

# Define variables to optimize
cx = tf.Variable(0.0, tf.float32)
cy = tf.Variable(0.0, tf.float32)
r = tf.Variable(1.0, tf.float32)

# Define loss function (least squares residuals)
def loss(cx,cy,r):
    return tf.norm((x_vals - cx)**2 + (y_vals - cy) ** 2 - r ** 2)

loss_fn = lambda: loss(cx,cy,r)

# Iterate gradient descent to optimize variables
for i in range(500):
    opt.minimize(loss_fn, [cx,cy,r])
    print('cx = {:.3f}, cy = {:.3f}, r = {:.3f}, cost = {:.3f}'.format(
        cx.numpy(),cy.numpy(),r.numpy(),loss(cx,cy,r).numpy()
    ))

# Display results
plt.plot(x_vals, y_vals, 'r+', label='data')
plt.xlabel('x')
plt.ylabel('y')
circle = plt.Circle((cx.numpy(), cy.numpy()), r.numpy(), color='b', fill=False)
plt.gcf().gca().add_artist(circle)
plt.show()
