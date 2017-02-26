# This is the prediction algorithm to foresee the comparative consumption, impletement by TensorFlow
import tensorflow as tf
import json, csv
import output

month = []
amount = []
with open('data.csv') as datafile:
	reader = csv.DictReader(datafile)
	for row in reader:
		month.append(float(row['month']))
		amount.append(float(row['amount']))

# Model parameters
a = tf.Variable([1.], tf.float32)
b = tf.Variable([1.], tf.float32)
c = tf.Variable([1.], tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
# linear_model = a*x**2 + b*x + c
linear_model = a*x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
  # sess.run(train, {x:month, y:amount})
  sess.run(train, {x:month, y:amount})

# evaluate training accuracy
# curr_a, curr_b, curr_c, curr_loss  = sess.run([a, b, c, loss], {x:[1,2,3,4], y:[9,6,4,2]})
# print("a: %s b: %s c: %s loss: %s"%(curr_a, curr_b, curr_c, curr_loss))
curr_a, curr_b, curr_loss  = sess.run([a, b, loss], {x:month, y:amount})
print("a: %s b: %s loss: %s"%(curr_a, curr_b, curr_loss))
