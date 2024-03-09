import numpy as np

# Load the data from the CSV file
data = np.genfromtxt('Transactions.csv', delimiter=',', skip_header=1, dtype=str)

# Separate the features and labels
X = np.column_stack((data[:, 1:4].astype(float), data[:, 4].astype(float)))
y = (data[:, -1] == 'Yes').astype(int)

# Add a bias term to the features
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Initialize the weights and learning rate
weights = np.zeros(X.shape[1])
learning_rate = 0.1

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the perceptron training function
def train_perceptron(X, y, weights, learning_rate, num_epochs):
    for epoch in range(num_epochs):
        y_pred = sigmoid(np.dot(X, weights))
        error = y - y_pred
        weights += learning_rate * np.dot(X.T, error)
    return weights

# Train the perceptron
num_epochs = 1000
final_weights = train_perceptron(X, y, weights, learning_rate, num_epochs)

# Evaluate the perceptron on the training data
y_pred = sigmoid(np.dot(X, final_weights))
y_pred = (y_pred >= 0.5).astype(int)
accuracy = np.mean(y_pred == y)
print(f"Training accuracy: {accuracy * 100:.2f}%")

# Print the final weights
print("Final weights:")
print(final_weights)