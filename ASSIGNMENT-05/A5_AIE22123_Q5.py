import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

r"Food Ingredients and Recipe Dataset with Image Name Mapping.csv"
file = pd.read_csv(r"Food Ingredients and Recipe Dataset with Image Name Mapping.csv"
)

file['X'] = file['Ingredients'].apply(len)
file['Y'] = file['Instructions'].astype(str).apply(len)  

threshold = 8  
file['Class'] = np.where(file['X'] + file['Y'] > threshold, 1, 0)

X_test = np.arange(0, 10.1, 0.1)
Y_test = np.arange(0, 10.1, 0.1)
test_grid = np.array(np.meshgrid(X_test, Y_test)).T.reshape(-1, 2)

test_data = pd.DataFrame(test_grid, columns=['X', 'Y'])

k_values = [1, 3, 5, 7]  
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for i, k in enumerate(k_values, 1):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(file[['X', 'Y']], file['Class'])
    test_data[f'Predicted_Class_{k}'] = knn_classifier.predict(test_data[['X', 'Y']])

    ax = axes[(i - 1) // 2, (i - 1) % 2]
    colors = {0: 'blue', 1: 'red'}
    ax.scatter(test_data['X'], test_data['Y'], c=test_data[f'Predicted_Class_{k}'].map(colors),
               label=f'k={k} - Predicted Class', alpha=0.5)
    ax.scatter(file['X'], file['Y'], c=file['Class'].map(colors), marker='x',
               label=file['Class'].map({0: 'Class 0 (Blue)', 1: 'Class 1 (Red)'}))
    ax.set_title(f'Scatter Plot of Test Data (k={k})')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()

plt.tight_layout()
plt.show()