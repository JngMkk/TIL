import matplotlib.pyplot as plt
from random import randint
import numpy as np

fig, ax = plt.subplots()
x = list(randint(0, 1000) for _ in range(10))
print(x)
print(f'평균: {np.mean(x)}')
print(f'중위값: {np.median(x)}')

ax.boxplot(x)
plt.show()