import matplotlib.pyplot as plt
from random import randint

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

x = [1, 2, 3, 4, 5]
y = list(randint(1, 100) for _ in range(5))

ax1.bar(x, y, color='r')
ax2.barh(x, y, color='b')

plt.show()