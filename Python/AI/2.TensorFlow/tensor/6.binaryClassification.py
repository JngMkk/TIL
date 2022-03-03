import tensorflow as tf

# 1. 데이터 준비
X_data = [
    [1, 0],
    [2, 0],
    [5, 1],
    [2, 3],
    [3, 3],
    [8, 1],
    [10, 0]
]
y_data = [
    [0],
    [1],
    [0],
    [0],
    [1],
    [1],
    [1]
]

X = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 2. 가설 설정
W = tf.Variable(tf.random_normal([2, 1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

# sigmoid : 0 ~ 1 사이의 실수 (H > 0.5 : true) => 0 / 1
logit = tf.matmul(X, W) + b
H = tf.sigmoid(logit)

# 3. 준비
# loss function
# loss 값을 미분했을 때 0이 되는 지점이 하나가 아님
# nn : neural network
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits= logit, labels=y))

# optimizer
learning_rate = 0.1
opti = tf.train.GradientDescentOptimizer(learning_rate)
train = opti.minimize(loss)

# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 10000
for step in range(epochs):
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X: X_data, y: y_data})
    print(f'W:{W_val.reshape(1,2)} \t b: {b_val} \t loss:{loss_val}')

# 5. 예측
print(sess.run(H, feed_dict={X: [[4, 2], [2, 4]]}).reshape(1, 2))