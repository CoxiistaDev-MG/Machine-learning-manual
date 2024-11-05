from tools import data, backpropagation
from random import random

data.DATA_FILE = 'tools/data/'
iris = data.DataSet('iris.csv', 1)

''''n1 = backpropagation.Network((iris.len_inputs, 4, iris.len_results), ['sigmoid'], True)
n1.trainer_weights_mini_batch(iris.trainer, iris.trainer_results,10, 100, 1, True)
#n1.trainer_weights_stochastic(iris.trainer, iris.trainer_results, 1000, 1)
'''
'''n2 = backpropagation.Network((3, 2), ['tangh'])
n2.trainer_weights_mini_batch(data=[
        backpropagation.Matrix([[0], [0], [0]]),
        backpropagation.Matrix([[1], [0], [0]]),
        backpropagation.Matrix([[0], [1], [0]]),
        backpropagation.Matrix([[1], [1], [1]])
                                        ], responses=[0, 1, 1, 0], len_mini_batch=1, eppochs=100, lr=0.5)


'''


n3 = backpropagation.Network((1, 1), [], False)

lst = []
resp = []
for each in range(150):
    rad = random()
    lst.append(backpropagation.Matrix([[rad]]))
    resp.append(rad*1.8 + 32)

print(lst)
n3.trainer_weights_mini_batch(lst, resp, 1, 1000, 0.01)
print(n3.biases)
print(n3.weights)