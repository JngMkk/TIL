import tensorflow as tf

# placeholder : 그래프를 실행하는 시점에 데이터를 입력받을 수 있도록
node1 = tf.placeholder(dtype=tf.float32)
node2 = tf.placeholder(dtype=tf.float32)

node3 = node1 + node2

sess = tf.Session()

# data 입력해주면서 실행
X = [10, 20, 30]
y = [40, 50, 60]

print(sess.run(node3, feed_dict={node1 : X, node2 : y}))