import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def derivative_sigmoid(x):
  return sigmoid(x) * (1 - sigmoid(x))

def initialize_weights(input_size, hidden_size):
  W1 = np.random.rand(input_size, hidden_size)
  b1 = np.random.rand(hidden_size)
  W2 = np.random.rand(hidden_size, 1)
  b2 = np.random.rand()
  return W1, b1, W2, b2

def feedforward(X, W1, b1, W2, b2):
  A1 = sigmoid(np.dot(X, W1) + b1)
  H2 = sigmoid(np.dot(A1, W2) + b2)
  return A1, H2

def backpropagation(X, y, A1, H2, W1, W2, b1, b2, learning_rate):
  dH2 = H2 - y
  dW2 = np.dot(A1.T, dH2) * learning_rate
  db2 = np.sum(dH2) * learning_rate
  dA1 = np.dot(dH2, W2.T) * derivative_sigmoid(A1)
  dW1 = np.dot(X.T, dA1) * learning_rate
  db1 = np.sum(dA1) * learning_rate
  return dW1, db1, dW2, db2

def train(X, y, learning_rate, epochs):
  W1, b1, W2, b2 = initialize_weights(2, 1)
  for epoch in range(epochs):
    A1, H2 = feedforward(X, W1, b1, W2, b2)
    dW1, db1, dW2, db2 = backpropagation(X, y, A1, H2, W1, W2, b1, b2, learning_rate)
    W1 -= dW1
    b1 -= db1
    W2 -= dW2
    b2 -= db2
    
    if np.mean(np.abs(y - H2)) <= 0.002:
      break

  return W1, b1, W2, b2

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])
learning_rate = 0.05
epochs = 1000

W1, b1, W2, b2 = train(X, y, learning_rate, epochs)

y_pred = feedforward(X, W1, b1, W2, b2)[1]
print(y_pred)
