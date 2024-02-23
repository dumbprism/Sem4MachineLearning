import pandas as pd
import numpy as np

file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

file.dropna(subset=['Title'], inplace=True)

class_a_data = file[file['Title'].str.contains('Crispy Salt and Pepper Potatoes', na=True)].copy()
class_b_data = file[file['Title'].str.contains('Turmeric Hot Toddy', na=True)].copy()

def clean_and_tokenize(ingredients):
    ingredients = ingredients.replace("[", "").replace("]", "").replace("'", "")
    ingredients = ingredients.split(",")
    return [ingredient.strip() for ingredient in ingredients]

class_a_data['Instructions'] = class_a_data['Instructions'].apply(clean_and_tokenize)
class_b_data['Instructions'] = class_b_data['Instructions'].apply(clean_and_tokenize)

class_a_intraclass_spread = np.nan
class_b_intraclass_spread = np.nan

if len(class_a_data) > 1:
    class_a_cov_matrix = np.cov(class_a_data['Ingredients'].apply(len), rowvar=False)
    class_a_intraclass_spread = np.trace(class_a_cov_matrix)

if len(class_b_data) > 1:
    class_b_cov_matrix = np.cov(class_b_data['Ingredients'].apply(len), rowvar=False)
    class_b_intraclass_spread = np.trace(class_b_cov_matrix)

class_a_mean_vector = np.mean(class_a_data['Ingredients'].apply(len), axis=0)
class_b_mean_vector = np.mean(class_b_data['Ingredients'].apply(len), axis=0)
interclass_distance = np.linalg.norm(class_a_mean_vector - class_b_mean_vector)

print("Intraclass spread for Class A:", class_a_intraclass_spread)
print("Intraclass spread for Class B:", class_b_intraclass_spread)
print("Interclass distance between Class A and Class B:", interclass_distance)
