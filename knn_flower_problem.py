from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
print(iris.target)
print(type(iris))
iris_np = np.array(iris)
print(iris_np)
print(type(iris_np))
var = iris.data.shape
print(var)

'''create a array of idx in len iris and shuffle it'''
idx = np.arange(len(iris.data))
np.random.shuffle(idx)

'''split idx for two parts 80% and 20%'''
split_data = int(0.8 * len(idx))
eighty_present = idx[:split_data]
twenty_present = idx[split_data:]

''''''
X_train = iris.data[eighty_present]
x_test = iris.data[twenty_present]
y_train = iris.target[eighty_present]
y_test = iris.target[twenty_present]

