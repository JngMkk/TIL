import tensorflow as tf
from tensorflow_core.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('data/mnist/', one_hot=True)

X = tf.placeholder(shape=[None, 784], dtype = tf.float32)
y = tf.placeholder(shape=[None, 10], dtype = tf.float32)

W1 = tf.Variable(tf.random_normal([784, 256]), name='weight1')
b1 = tf.Variable(tf.random_normal([256]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([256, 256]), name = 'weight2')
b2 = tf.Variable(tf.random_normal([256]), name = 'bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([256, 10]), name = 'weight3')
b3 = tf.Variable(tf.random_normal([10]), name = 'bias3')

logit = tf.matmul(layer2, W3) + b3
H = tf.nn.relu(logit)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit, labels=y))

train = tf.train.AdamOptimizer(0.001).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

num_of_epoch = 30
batch_size = 100
for step in range(num_of_epoch):
    total_iter = int(mnist.train.num_examples / batch_size)
    for i in range(total_iter):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        _, loss_val = sess.run([train, loss], feed_dict = {X:batch_x, y: batch_y})
        if step % 3 == 0:
            print(f'loss: {loss_val}')

predict = tf.argmax(H, 1)
correct = tf.equal(predict, tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))
print(f'acc: {sess.run(accuracy, feed_dict={X:mnist.test.images, y: mnist.test.labels})}')