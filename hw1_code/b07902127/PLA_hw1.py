import numpy as np
import requests
import random
from matplotlib import pyplot as plt

def GetData(url):
    response = requests.get(url)
    data = response.content.decode('utf-8')
    x = []
    y = []
    data = data.split('\n')
    for line in data[0 : -1]:
        cut = line.split('\t')
        data_x = cut[0].split(' ')
        data_y = int(cut[1])
        for i in range(4):
            data_x[i] = float(data_x[i])
        x.append([1] + data_x)
        y.append(data_y)
    x = np.array(x)
    y = np.array(y)
    return x, y

def sign(w, x):
	if np.dot(w, x) > 0:
		return 1
	else:
		return -1

def one_Performance(x, y, w, turn):
	update_num = 0
	num_of_x = len(x)
	index = list(range(num_of_x))
	random.shuffle(index)
	for i in index:
		val = sign(w, x[i])
		if val != y[i]:
			update_num += 1
			w += y[i] * x[i]
			turn += 1
	return update_num, turn

def PLA_for_problem6():
	url = 'http://www.csie.ntu.edu.tw/~htlin/course/mlfound19fall/hw1/hw1_6_train.dat'
	x,y = GetData(url)
	total = 0
	frequency = []
	update = []
	for i in range(1, 1127):
		w = np.zeros((5), dtype = float)
		turn = 0
		sum_ = 0
		cnt, turn = one_Performance(x, y, w, turn)
		while cnt != 0:
			sum_ += cnt
			cnt, turn = one_Performance(x, y, w, turn)
		total += sum_
		update.append(sum_)

	''' #Remove the comment to see the histogram for problem 6
    # Only allow to see a histogram for one problem a time

	plt.hist(update, facecolor = 'purple', alpha = 0.5)
	plt.xlabel('number of updates')
	plt.ylabel('frequency of the number')
	plt.show()

	'''
	print('Average number of update =', total/1126)
	
def Pocket(times, x, y, w):
	num_of_x = len(x)
	index = list(range(num_of_x))
	turns = 0
	while turns < times:
		tmp_w = w
		random.shuffle(index)
		for i in index:
			val = sign(tmp_w, x[i])
			if val != y[i]:
				turns += 1
				tmp_w = tmp_w + y[i] * x[i]
#               after-fixed w
				err_fix = 0
				for j in range(num_of_x):
					v1 = sign(tmp_w, x[j])
					if v1 != y[j]:
						err_fix += 1
#               original w
				err_org = 0
				for j in range(num_of_x):
					v2 = sign(w, x[j])
					if v2 != y[j]:
						err_org += 1
				if err_fix < err_org:
					for i in range(5):
						w[i] = tmp_w[i]
			if turns == times:
				break
	return w
					
def PLA_for_problem7():
	train = 'http://www.csie.ntu.edu.tw/~htlin/course/mlfound19fall/hw1/hw1_7_train.dat'
	test = 'http://www.csie.ntu.edu.tw/~htlin/course/mlfound19fall/hw1/hw1_7_test.dat'
	train_x, train_y = GetData(train)
	test_x, test_y = GetData(test)
	err_rate_sum = 0
	ans = []
	for i in range(1, 1127):
		w = np.zeros((5), dtype = float)
		w = Pocket(100, train_x, train_y, w)
		cnt = 0
		num_of_testx = len(test_x)
		for j in range(num_of_testx):
			val = sign(w, test_x[j])
			if val != test_y[j]:
				cnt += 1
		cnt /= num_of_testx
		ans.append(cnt)
		err_rate_sum += cnt

	''' #Remove the comment when testing problem 7
	# Only allow to see a histogram for one problem a time

	plt.hist(ans, facecolor = 'yellow', alpha = 0.6)
	plt.xlabel('error rate')
	plt.ylabel('frequency')
	plt.show()

	'''
	print('Average error rate =', err_rate_sum/1126)
	
def PLA(times, x, y, w):
	num_of_x = len(x)
	index = list(range(num_of_x))
	turns = 0
	while turns < times:
		random.shuffle(index)
		for i in index:
			val = sign(w, x[i])
			if val != y[i]:
				turns += 1
				w = w + y[i] * x[i]
			if turns == times:
				break
	return w

def PLA_for_problem8():
	train = 'http://www.csie.ntu.edu.tw/~htlin/course/mlfound19fall/hw1/hw1_7_train.dat'
	test = 'http://www.csie.ntu.edu.tw/~htlin/course/mlfound19fall/hw1/hw1_7_test.dat'
	train_x, train_y = GetData(train)
	test_x, test_y = GetData(test)
	err_rate_sum = 0
	ans = []
	for i in range(1, 1127):
		w = np.zeros((5), dtype = float)
		w = PLA(100, train_x, train_y, w)
		cnt = 0
		num_of_testx = len(test_x)
		for j in range(num_of_testx):
			val = sign(w, test_x[j])
			if val != test_y[j]:
				cnt += 1
		cnt /= num_of_testx
		ans.append(cnt)
		err_rate_sum += cnt
	
	''' #Remove the comment when testing problem 8
	# Only allow to see a histogram for one problem a time

	plt.hist(ans, facecolor = 'blue', alpha = 0.6)
	plt.xlabel('error rate')
	plt.ylabel('frequency')
	plt.show()

	'''
	print('Average error rate =', err_rate_sum/1126)


if __name__ == '__main__':
	PLA_for_problem6()
	PLA_for_problem7()
	PLA_for_problem8()
	
