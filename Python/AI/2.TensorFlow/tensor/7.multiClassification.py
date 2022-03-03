import tensorflow as tf

# 1. 데이터 준비
# 4번의 쪽지시험 -> 상 / 중 / 하
X_data = [
    [10, 7, 8, 3],
    [8, 8, 9, 4],
    [7, 8, 2, 3],
    [6, 3, 9, 3],
    [7, 6, 7, 5],
    [3, 5, 6, 2],
    [2, 4, 3, 1]
]
y_data = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 1]
]
X = tf.placeholder(shape=[None, 4], dtype=tf.float32)
y = tf.placeholder(shape=[None, 3], dtype=tf.float32)

# 2. 가설 설정
W = tf.Variable(tf.random_normal([4, 3]), name = 'weight')
b = tf.Variable(tf.random_normal([3]), name = 'bias')

logit = tf.matmul(X, W) + b
H = tf.nn.softmax(logit)
 
# 3. 모델 준비
# loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits = logit, labels=y))

# optimizer
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 3000
for step in range(epochs):
    _, loss_val = sess.run([train, loss], feed_dict={X: X_data, y: y_data})
    print(f'loss:{loss_val}')

# 5. 예측 / 평가
print(sess.run(H, feed_dict={X: [[4, 9, 8, 5]]}))