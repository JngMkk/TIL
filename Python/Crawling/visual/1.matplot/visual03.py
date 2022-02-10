import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

x = [1, 2, 3, 4, 5]
y1 = list(map(lambda x: x**2, x))
y2 = list(map(lambda x: x**3, x))

ax1.plot(x, y1, c='r', label='power2')
ax2.plot(x, y2, c='b', label='power3')
ax1.legend()
ax2.legend()
ax1.set_title("x**2")
ax2.set_title("x**3")
ax1.set_ylim(0,100)
ax2.set_ylim(0,100)
plt.show()