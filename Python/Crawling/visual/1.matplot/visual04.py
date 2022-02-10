import matplotlib.pyplot as plt
import random

"""
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
...
...
"""

fig, ax = plt.subplots(2, 2, figsize=(10, 10))
x = list(range(50))
y1 = list(random.randint(0, 50) for _ in range(50))
y2 = list(random.randint(0, 50) for _ in range(50))
y3 = list(random.randint(0, 50) for _ in range(50))
y4 = list(random.randint(0, 50) for _ in range(50))

# 산점도(scatter plot)

ax[0, 0].scatter(x, y1, c='r')
ax[0, 1].scatter(x, y2, c='g')
ax[1, 0].scatter(x, y3, c='b')
ax[1, 1].scatter(x, y4, c='y')

ax[0, 0].set_title('y1')
ax[0, 1].set_title('y2')
ax[1, 0].set_title('y3')
ax[1, 1].set_title('y4')

fig.tight_layout()
plt.show()