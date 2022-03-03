import tensorflow as tf

# 1. 데이터 준비
X_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
y_data = [
    [0],
    [1],
    [1],
    [0]
]
X = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 2. 가설 검정
W = tf.Variable(tf.random_normal([2, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

logit = tf.matmul(X, W) + b
H = tf.sigmoid(logit)

# 3. 준비
# loss function
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=y))

# optimizer
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 30000
for step in range(epochs):
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X:X_data, y:y_data})
    print(f'W:{W_val.reshape(1, 2)} \t b: {b_val} \t loss:{loss_val}')

# 5. 예측
print(sess.run(H, feed_dict={X: X_data}))