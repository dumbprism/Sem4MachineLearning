import numpy as np

def step_activation(x):
    return 1 if x >= 0 else 0

def bipolar_step_activation(x):
    return 1 if x >= 0 else -1

def sigmoid_activation(x):
    return 1 / (1 + np.exp(-x))

def relu_activation(x):
    return max(0, x)

def perceptron_gate(X, y, weights, activation, learning_rate, max_epochs):
    errors = []
    for epoch in range(max_epochs):
        total_error = 0
        for x, target in zip(X, y):
            output = activation(np.dot(weights, x))
            error = target - output
            total_error += error**2
            weights += learning_rate * error * x
        errors.append(total_error)
        if total_error == 0:
            break
    print(f"Weights: {weights}, Epochs: {epoch + 1}")
    return weights, errors

X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

weights_and = np.random.rand(2)  
learning_rate = 0.1
max_epochs = 100

# Using step activation function
weights_and_step, errors_and_step = perceptron_gate(X_and, y_and, weights_and, step_activation, learning_rate, max_epochs)
print("Final Weights for AND Gate (Step Activation):", weights_and_step)
print("Errors during training (Step Activation):", errors_and_step)

# Using bipolar step activation function
weights_and_bipolar, errors_and_bipolar = perceptron_gate(X_and, y_and, weights_and, bipolar_step_activation, learning_rate, max_epochs)
print("Final Weights for AND Gate (Bipolar Step Activation):", weights_and_bipolar)
print("Errors during training (Bipolar Step Activation):", errors_and_bipolar)

# Using sigmoid activation function
weights_and_sigmoid, errors_and_sigmoid = perceptron_gate(X_and, y_and, weights_and, sigmoid_activation, learning_rate, max_epochs)
print("Final Weights for AND Gate (Sigmoid Activation):", weights_and_sigmoid)
print("Errors during training (Sigmoid Activation):", errors_and_sigmoid)

# Using ReLU activation function
weights_and_relu, errors_and_relu = perceptron_gate(X_and, y_and, weights_and, relu_activation, learning_rate, max_epochs)
print("Final Weights for AND Gate (ReLU Activation):", weights_and_relu)
print("Errors during training (ReLU Activation):", errors_and_relu)
