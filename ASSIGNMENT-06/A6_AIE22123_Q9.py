import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
class NeuralNetwork:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = 4
        self.lr = 0.1
        self.weights_input_hidden = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (self.hidden_size, self.output_size))

    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden)
        self.hidden_output = sigmoid(self.hidden_input)
        self.output = sigmoid(np.dot(self.hidden_output, self.weights_hidden_output))
        return self.output

    def backward(self, X, y, output):
    
        error = y - output
        d_output = error * sigmoid_derivative(output)
        error_hidden = d_output.dot(self.weights_hidden_output.T)
        d_hidden = error_hidden * sigmoid_derivative(self.hidden_output)
        self.weights_hidden_output += self.hidden_output.T.dot(d_output) * self.lr
        self.weights_input_hidden += X.T.dot(d_hidden) * self.lr

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if epoch % 1000 == 0:
                print("Epoch:", epoch)
                print("Loss:", np.mean(np.abs(y - output)))
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([[1, 0], [1, 0], [1, 0], [0, 1]])
y_or = np.array([[1, 0], [0, 1], [0, 1], [0, 1]])
y_xor = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])

print("Training AND gate neural network:")
and_nn = NeuralNetwork(2, 2)
and_nn.train(X, y_and, 10000)
print("\nTraining OR gate neural network:")
or_nn = NeuralNetwork(2, 2)
or_nn.train(X, y_or, 10000)
print("\nTraining XOR gate neural network:")
xor_nn = NeuralNetwork(2, 2)
xor_nn.train(X, y_xor, 10000)
print("\nTesting the trained models:")
print("AND gate predictions:", and_nn.forward(X))
print("OR gate predictions:", or_nn.forward(X))
print("XOR gate predictions:", xor_nn.forward(X))
