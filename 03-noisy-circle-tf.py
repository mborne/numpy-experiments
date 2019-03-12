import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

xy=np.loadtxt(open("data/noisy-circle.csv", "rb"), delimiter=",", skiprows=1)

x_vals=xy[:,0]
y_vals=xy[:,1]


# x and y are placeholders for our training data
x = tf.placeholder("float")
y = tf.placeholder("float")

# w is the variable storing our values. It is initialised with starting "guesses"
# w[0] : cx
# w[1] : cy
# w[2] : r
w = tf.Variable([0.0, 0.0, 1.0], name="w")

# model : (x - cx)^2 + (y - cy)^2 - r^2 = 0
delta = tf.subtract(
    tf.add(
        tf.square( tf.subtract( x, w[0] ) ),
        tf.square( tf.subtract( y, w[1] ) )
    ), tf.square(w[2])
)

error = tf.abs(delta)


# Normal TensorFlow - initialize values, create a session and run the model
model = tf.global_variables_initializer()

# The Gradient Descent Optimizer does the heavy lifting
train_op = tf.train.GradientDescentOptimizer(0.001).minimize(error)

with tf.Session() as session:
    session.run(model)
    for k in range(100):
        for i in range(x_vals.size):
            session.run(train_op, feed_dict={x: x_vals[i], y: y_vals[i]})
        w_value = session.run(w)
        print("Predicted model: cx={cx:.3f}, cy={cy:.3f}, r={r:.3f}".format(cx=w_value[0], cy=w_value[1], r=w_value[2]))

plt.plot(x_vals, y_vals, 'r+', label='data')
plt.xlabel('x')
plt.ylabel('y')

circle = plt.Circle((w_value[0], w_value[1]), w_value[2], color='b', fill=False)
plt.gcf().gca().add_artist(circle)

plt.show()
