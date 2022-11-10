from matplotlib import pyplot as plt

f = open('./p7', 'r')
data = []

for i in range(1000):
	data.append(float(f.readline()))

plt.hist(data, facecolor = 'yellow', alpha = 0.5)
plt.xlabel('Ein - Eout')
plt.ylabel('frequency')
plt.show()

