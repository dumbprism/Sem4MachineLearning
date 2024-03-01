import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv(r"Food Ingredients and Recipe Dataset with Image Name Mapping.csv")

file['Instructions'].fillna('', inplace=True)

file['X'] = file['Ingredients'].apply(len)
file['Y'] = file['Instructions'].apply(len)

np.random.seed(42)  
num_points = 20

X_values = np.random.randint(1, 11, num_points)
Y_values = np.random.randint(1, 11, num_points)

threshold = 12  
classes = np.where(X_values + Y_values > threshold, 1, 0)

random_data = pd.DataFrame({'X': X_values, 'Y': Y_values, 'Class': classes})

colors = {0: 'blue', 1: 'red'}
plt.scatter(random_data['X'], random_data['Y'], c=random_data['Class'].map(colors),
            label=random_data['Class'].map({0: 'Class 0 (Blue)', 1: 'Class 1 (Red)'}))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Random Data')
plt.legend()
plt.show()