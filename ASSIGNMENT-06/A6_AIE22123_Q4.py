import numpy as np

def step_activation(x):
    return 1 if x >= 0 else 0

def perceptron_gate(X, y, weights, learning_rate, max_epochs):
    errors = []
    for epoch in range(max_epochs):
        total_error = 0
        for x, target in zip(X, y):
            output = step_activation(np.dot(weights, x))
            error = target - output
            total_error += error**2
            weights += learning_rate * error * x
        errors.append(total_error)
        if total_error == 0:
            break
    print(f"Weights: {weights}, Epochs: {epoch + 1}")
    return weights, errors

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])


weights_xor = np.random.rand(2)  

learning_rate = 0.1
max_epochs = 100

weights_xor, errors_xor = perceptron_gate(X_xor, y_xor, weights_xor, learning_rate, max_epochs)
print("Final Weights for XOR Gate:", weights_xor)
print("Errors during training:", errors_xor)


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

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

weights_xor = np.random.rand(2)  
learning_rate = 0.1
max_epochs = 100

weights_xor_step, errors_xor_step = perceptron_gate(X_xor, y_xor, weights_xor, step_activation, learning_rate, max_epochs)
print("Final Weights for XOR Gate (Step Activation):", weights_xor_step)
print("Errors during training (Step Activation):", errors_xor_step)

weights_xor_bipolar, errors_xor_bipolar = perceptron_gate(X_xor, y_xor, weights_xor, bipolar_step_activation, learning_rate, max_epochs)
print("Final Weights for XOR Gate (Bipolar Step Activation):", weights_xor_bipolar)
print("Errors during training (Bipolar Step Activation):", errors_xor_bipolar)

weights_xor_sigmoid, errors_xor_sigmoid = perceptron_gate(X_xor, y_xor, weights_xor, sigmoid_activation, learning_rate, max_epochs)
print("Final Weights for XOR Gate (Sigmoid Activation):", weights_xor_sigmoid)
print("Errors during training (Sigmoid Activation):", errors_xor_sigmoid)

weights_xor_relu, errors_xor_relu = perceptron_gate(X_xor, y_xor, weights_xor, relu_activation, learning_rate, max_epochs)
print("Final Weights for XOR Gate (ReLU Activation):", weights_xor_relu)
print("Errors during training (ReLU Activation):", errors_xor_relu)


import numpy as np

def step_activation(x):
    return 1 if x >= 0 else 0

def perceptron_gate(X, y, weights, learning_rate, max_epochs):
    errors = []
    for epoch in range(max_epochs):
        total_error = 0
        for x, target in zip(X, y):
            output = step_activation(np.dot(weights, x))
            error = target - output
            total_error += error**2
            weights += learning_rate * error * x
        errors.append(total_error)
        if total_error == 0:
            break
    print(f"Weights: {weights}, Epochs: {epoch + 1}")
    return weights, errors

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

weights_xor = np.random.rand(2)  
learning_rate = 0.1
max_epochs = 100

weights_xor, errors_xor = perceptron_gate(X_xor, y_xor, weights_xor, learning_rate, max_epochs)
print("Final Weights for XOR Gate:", weights_xor)
print("Errors during training:", errors_xor)

def perceptron_xor_gate_varying_lr(X, y, weights, learning_rates, max_epochs):
    iterations = []
    for lr in learning_rates:
        weights_lr = weights.copy()
        epoch = 0
        for epoch in range(max_epochs):
            total_error = 0
            for x, target in zip(X, y):
                output = step_activation(np.dot(weights_lr, x))
                error = target - output
                total_error += error**2
                weights_lr += lr * error * x
            if total_error <= 0.002:
                break
        iterations.append(epoch + 1)
    print("Epochs for different learning rates:", iterations)
    return iterations

learning_rates = [0.1, 0.01, 0.001]
max_epochs = 100
iterations_xor = perceptron_xor_gate_varying_lr(X_xor, y_xor, weights_xor, learning_rates, max_epochs)

