from tools import data, backpropagation
from random import random

data.DATA_FILE = 'tools/data/'

matrix = backpropagation.Matrix
lst = [matrix([[1, 3.5]]), matrix([[1.9, 2.7]]), matrix([[3, 2.5]]), matrix([[4.1, 1.1]]), matrix([[5, 0.7]])]
resp = [11, 11.2, 12.8, 12.4, 13.7]

n = backpropagation.Network((2, 1), [], False)

n.trainer_weights_mini_batch(lst, resp, 1, 10000, 0.03)
print(n.weights)
print(n.biases)