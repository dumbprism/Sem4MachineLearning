import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

file = pd.read_csv(r"Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

threshold = 8

np.random.seed(42)
num_points = 20
X_train = np.random.uniform(1, 10, num_points)
Y_train = np.random.uniform(1, 10, num_points)
classes_train = np.where(X_train + Y_train > threshold, 1, 0)

colors_train = {0: 'blue', 1: 'red'}
plt.scatter(X_train, Y_train, c=np.vectorize(colors_train.get)(classes_train),
            label=np.vectorize({0: 'Class 0 (Blue)', 1: 'Class 1 (Red)'}.get)(classes_train))
plt.xlabel('Ingredients Length')
plt.ylabel('Instructions Length')
plt.title('Scatter Plot of Training Data')
plt.legend()
plt.show()

X_test = np.arange(0, 10.1, 0.1)
Y_test = np.arange(0, 10.1, 0.1)
test_grid = np.array(np.meshgrid(X_test, Y_test)).T.reshape(-1, 2)

test_data = pd.DataFrame(test_grid, columns=['Ingredients Length', 'Instructions Length'])

knn_classifier = KNeighborsClassifier(n_neighbors=3)
file['Ingredients Length'] = file['Ingredients'].apply(len)
file['Instructions Length'] = file['Instructions'].apply(len)

knn_classifier.fit(file[['Ingredients Length', 'Instructions Length']], file['Class'])

test_data['Ingredients Length'] = test_data['Ingredients Length'].apply(len)
test_data['Instructions Length'] = test_data['Instructions Length'].apply(len)

test_data['Predicted_Class'] = knn_classifier.predict(test_data[['Ingredients Length', 'Instructions Length']])

colors_test = {0: 'blue', 1: 'red'}
plt.scatter(test_data['Ingredients Length'], test_data['Instructions Length'],
            c=np.vectorize(colors_test.get)(test_data['Predicted_Class']),
            label=np.vectorize({0: 'Class 0 (Blue)', 1: 'Class 1 (Red)'}.get)(test_data['Predicted_Class']))
plt.xlabel('Ingredients Length')
plt.ylabel('Instructions Length')
plt.title('Scatter Plot of Test Data (k=3)')
plt.legend()
plt.show()

k_values = [1, 3, 5, 7]  
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for i, k in enumerate(k_values, 1):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(file[['Ingredients Length', 'Instructions Length']], file['Class'])
    test_data[f'Predicted_Class_{k}'] = knn_classifier.predict(test_data[['Ingredients Length', 'Instructions Length']])

    ax = axes[(i - 1) // 2, (i - 1) % 2]
    ax.scatter(test_data['Ingredients Length'], test_data['Instructions Length'],
               c=np.vectorize(colors_test.get)(test_data[f'Predicted_Class_{k}']),
               label=np.vectorize({0: 'Class 0 (Blue)', 1: 'Class 1 (Red)'}.get)(test_data[f'Predicted_Class_{k}']), alpha=0.5)
    ax.set_title(f'Scatter Plot of Test Data (k={k})')
    ax.set_xlabel('Ingredients Length')
    ax.set_ylabel('Instructions Length')
    ax.legend()

plt.tight_layout()
plt.show()