from unicodedata import name
import tensorflow as tf

# 1. 데이터 준비
X = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 2. 가설설정
# H (hypothesis) = W(weight) * X + b(bias)
W = tf.Variable(tf.random_normal([1]), name = 'Weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

H = W * X + b

# 3. 모델 준비
# loss function
# MSE (Mean Square Error)
loss = tf.reduce_mean(tf.square(H - y))

# optimizer
# 경사 하강법 (gradient descent) : loss가 최소화 되는 값 찾기
# 0.01 : learning rate (얼만큼 움직일 것인가)
opti = tf.train.GradientDescentOptimizer(0.01)
train = opti.minimize(loss)     # loss가 최소가 되도록

# session
sess = tf.Session()

# 변수 초기화
sess.run(tf.global_variables_initializer())

# 4. 학습
# 학습 횟수
epochs = 5000
for step in range(epochs):
    tmp, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X: [1, 2, 3, 4, 5], y: [3, 5, 7, 9, 11]})
    if step % 100 == 0:
        print(loss_val, W_val, b_val)

# 5. 예측 / 평가
print(sess.run(H, feed_dict={X: [10, 11, 12, 13, 14]}))