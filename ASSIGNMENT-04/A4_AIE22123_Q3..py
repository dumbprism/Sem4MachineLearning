import pandas as pd
from scipy.spatial.distance import minkowski
import matplotlib.pyplot as plt

file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

feature_vectors = file['Ingredients'].tolist()

# Select any two feature vectors and flatten the lists
vector1 = ' '.join(map(str, feature_vectors[0]))
vector2 = ' '.join(map(str, feature_vectors[1]))

unique_ingredients = list(set(vector1.split() + vector2.split()))
vector1_numeric = [vector1.split().count(ingredient) for ingredient in unique_ingredients]
vector2_numeric = [vector2.split().count(ingredient) for ingredient in unique_ingredients]

r_values = list(range(1, 11))
distances = [minkowski(vector1_numeric, vector2_numeric, p=r) for r in r_values]

# Plot the graph
plt.plot(r_values, distances, marker='o')
plt.title('Minkowski Distance vs r')
plt.xlabel('r')
plt.ylabel('Distance')
plt.grid(True)
plt.show()