import numpy as np
import matplotlib.pyplot as plt

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
    return weights, epoch + 1

X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
weights_and = np.array([0.5, 0.5])  # Set initial weights to [0.5, 0.5]

def perceptron_and_gate_varying_lr(X, y, weights, learning_rates, max_epochs):
    iterations = []
    for lr in learning_rates:
        _, epoch = perceptron_gate(X, y, weights, lr, max_epochs)
        iterations.append(epoch)
    return iterations

learning_rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
max_epochs = 100
iterations = perceptron_and_gate_varying_lr(X_and, y_and, weights_and, learning_rates, max_epochs)

# Plot the number of iterations against the learning rates
plt.plot(learning_rates, iterations)
plt.xlabel('Learning Rate')
plt.ylabel('Number of Iterations')
plt.title('Convergence of Perceptron Learning')
plt.show()