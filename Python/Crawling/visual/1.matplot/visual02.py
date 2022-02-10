import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y1 = list(map(lambda x: x**2, x))
y2 = list(map(lambda x: x**3, x))

ax.plot(x, y1, c='r', label='power2')
ax.plot(x, y2, c='blue', label='power3')

plt.legend()

plt.show()
