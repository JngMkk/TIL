import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()

x = list(randint(0, 10) for _ in range(100))

ax.hist(x, bins=10)

plt.xticks(list(range(0, 11)))
plt.yticks(list(range(0, 101, 5)))

plt.xlim(0, 10)
plt.ylim(0, 30)

plt.show()