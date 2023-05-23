import numpy as np

#код нейрона
#функция активации
#Таким образом, активация нейрона это по сути мера того, насколько положительна соответствующая взвешенная сумма.
def sigmoid(x):
  # Наша функция активации: f(x) = 1 / (1 + e^(-x)) Чем больше абсолютное значение отрицательного входного числа, тем ближе выходное значение сигмоиды к нулю. Чем больше значение положительного входного числа, тем ближе значение функции к единице
  return 1 / (1 + np.exp(-x))

traning_input = np.array([[0,0,1],
                          [1,1,1],
                          [1,0,1],
                          [0,1,1]])

traning_output = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2*np.random.random((3,1))-1


#обучение нейронки методом обратного распространения
for i in range(20000):
  first_layer = traning_input
  second_layer = sigmoid(np.dot(first_layer, synaptic_weights))

  err_second_layer = traning_input - second_layer
  second_layer_delta = err_second_layer*sigmoid(second_layer)

  synaptic_weights = synaptic_weights + np.dot(first_layer.T, second_layer_delta)


print("weihgt: ")
print(synaptic_weights)

print("result: ")
print(second_layer)




# class Neuron:
#   def __init__(self, weights, bias):
#     self.weights = weights
#     self.bias = bias #Чтобы нейрон не активировался при малых положительных числах, можно добавить к взвешенной сумме некоторое отрицательное число – сдвиг (англ. bias), определяющий насколько большой должна быть взвешенная сумма, чтобы активировать нейрон

#   def feedforward(self, inputs):
#     # Умножаем входы на веса, прибавляем порог, затем используем функцию активации
#     total = np.dot(self.weights, inputs) + self.bias
#     return sigmoid(total)

# weights = np.array([0, 1]) # w1 = 0, w2 = 1
# bias = 4                   # b = 4
# n = Neuron(weights, bias)

# x = np.array([2, 3])       # x1 = 2, x2 = 3
# print(n.feedforward(x))    # 0.9990889488055994




# class OurNeuralNetwork:
#   '''
#   Нейронная сеть с:
#     - 2 входами
#     - скрытым слоем с 2 нейронами (h1, h2)
#     - выходным слоем с 1 нейроном (o1)
#   Все нейроны имеют одинаковые веса и пороги:
#     - w = [0, 1]
#     - b = 0
#   '''
#   def __init__(self):
#     weights = np.array([0, 1])
#     bias = 0

#     # Используем класс Neuron из предыдущего раздела
#     self.h1 = Neuron(weights, bias)
#     self.h2 = Neuron(weights, bias)
#     self.o1 = Neuron(weights, bias)

#   def feedforward(self, x):
#     out_h1 = self.h1.feedforward(x)
#     out_h2 = self.h2.feedforward(x)

#     # Входы для o1 - это выходы h1 и h2
#     out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

#     return out_o1

# network = OurNeuralNetwork()
# x = np.array([2, 3])
# print(network.feedforward(x)) # 0.7216325609518421

    
