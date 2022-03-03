import tensorflow as tf

# 상수 노드
node = tf.constant(100)

# session : 그래프를 실행시켜주는 역할 (runner)
sess = tf.Session()

print(sess.run(node))

"""
Tensorflow

- Tensor : 데이터 저장 객체 (placeholder)
- Variable : Weight, bias
- Operation : H = W * X + b (node, 식) -> 그래프
- Session : 그래프 실행 환경

"""