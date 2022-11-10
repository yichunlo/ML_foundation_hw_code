import matplotlib.pyplot as plt
import numpy as np

def gen_data(f):
	data = np.genfromtxt(f)
	x = data[:, :-1]
	x = np.c_[np.ones(x.shape[0]), x]
	y = data[:, -1].reshape(-1, 1)
	return x, y

def theta(s):
	return 1 / (np.exp(-s) + 1)

def grad(w, x, y):
	return np.mean(theta(-x.dot(w)*y)*x*y*(-1), axis = 0).reshape(-1, 1)

def get(w, x):
	y_cmp = x.dot(w)
	y_cmp[y_cmp <= 0] = -1
	y_cmp[y_cmp > 0 ] = 1
	return y_cmp

def myplot(iteration, GD, SGD, color1, color2, page):
	plt.plot(GD, color1, label = "GD", alpha = 0.8)
	plt.plot(SGD, color2, label = "SGD", alpha = 0.6)
	plt.xlabel('t')
	if page == 1:
		plt.ylabel('Ein(wt)')
	else:
		plt.ylabel('Eout(wt)')
	plt.show()

def run():
	x1, y1 = gen_data("./train.dat")
	x2, y2 = gen_data("./test.dat")
	iteration = 2000
	GD_w  = np.zeros((len(x1[0]), 1))
	SGD_w = np.zeros((len(x1[0]), 1))
	GD_Eout  = np.zeros(iteration)
	SGD_Eout = np.zeros(iteration)
	GD_Ein   = np.zeros(iteration)
	SGD_Ein  = np.zeros(iteration)
	for i in range(iteration):
		GD_w = GD_w - 0.01 * grad(GD_w, x1, y1)
		y1_cmp = get(GD_w, x1)
		y2_cmp = get(GD_w, x2)
		GD_Ein[i]  = np.mean(y1 != y1_cmp)
		GD_Eout[i] = np.mean(y2 != y2_cmp)

		x = x1[i%x1.shape[0], :]
		x = x.reshape(1, -1)
		y = y1[i%x1.shape[0], :]
		y = y.reshape(1, -1)
		SGD_w = SGD_w - 0.001 * grad(SGD_w, x, y)
		y1_cmp = get(SGD_w, x1)
		y2_cmp = get(SGD_w, x2)
		SGD_Ein[i]  = np.mean(y1 != y1_cmp)
		SGD_Eout[i] = np.mean(y2 != y2_cmp)
	
	myplot(iteration, GD_Ein,  SGD_Ein, 'm', 'cyan', 1)
	myplot(iteration, GD_Eout, SGD_Eout, 'c', 'orange', 2)
	
if __name__ == "__main__":
	run()
