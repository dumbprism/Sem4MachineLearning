import pandas as pd
from sklearn.model_selection import train_test_split
file =  pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')
print(file.columns)
y = df['Instructions']
class1 = 0  
class2 = 1  
subset_file = file[(y == class1) | (y == class2)]
X_train, X_test, y_train, y_test = train_test_split(
    subset_file['Ingredients'], subset_file[y], test_size=0.3, random_state=42
)
print("Training set size:", len(X_train))
print("Testing set size:", len(X_test))