import numpy as np
import pandas as pd

file_path = r'C:\Users\navee\Downloads\Transactions.xlsx'

try:
    df = pd.read_excel(file_path)
except Exception as e:
    print("Error reading Excel file:", e)
    raise SystemExit

print("Column Names:", df.columns)

df['High Value Tx?'] = df['High Value Tx?'].apply(lambda x: 1 if x == 'Yes' else -1)

X = df[['Candies (#)', 'Manogoes(Kg)', 'Milk Packets (#)', 'Payment(Rs)']].values
y = df['High Value Tx?'].values

X_bias = np.c_[np.ones(X.shape[0]), X]

def perceptron_learning(X, y, learning_rate=0.01, epochs=1000):
    weights = np.zeros(X.shape[1])
    for epoch in range(epochs):
        for i in range(X.shape[0]):
            if np.dot(X[i], weights) > 0:
                y_pred = 1
            else:
                y_pred = -1
            weights += learning_rate * (y[i] - y_pred) * X[i]
    return weights

perceptron_weights = perceptron_learning(X_bias, y)

pseudo_inverse_weights = np.linalg.pinv(X_bias) @ y

print("Weights from Perceptron Learning:", perceptron_weights)
print("Weights from Matrix Pseudo-Inverse:", pseudo_inverse_weights)