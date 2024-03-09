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
