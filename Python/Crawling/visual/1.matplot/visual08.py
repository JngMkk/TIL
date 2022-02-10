import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()

ages = list(randint(1, 100) for _ in range(100))
child = list(x for x in ages if x < 19)
young = list(x for x in ages if 19 <= x < 40)
middle = list(x for x in ages if 40 <= x < 60)
old = list(x for x in ages if x >= 60)

labels = ['child', 'young', 'middle', 'old']
count = [len(child), len(young), len(middle), len(old)]

ax.pie(count, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)

plt.show()