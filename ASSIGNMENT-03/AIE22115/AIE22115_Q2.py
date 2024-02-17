import pandas as pd
import numpy as np

# read the excel file 
file = pd.read_excel(r"C:\Users\navee\Downloads\Lab Session1 Data.xlsx",sheet_name="Purchase data")
A = file[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C = file['Payment (Rs)'].to_numpy().reshape(-1, 1)

# display the matrices A and C
print(f"A = {A}")
print(f"C = {C}")

# for finding the pseudo inverse of Matrix A
pseudo_inverse = np.linalg.pinv(A)

# for finding the model vector X for predicting the cost of the products
model_vector_X = np.dot(pseudo_inverse,C)
print(f"model vector X for predicting the cost of the products is = {model_vector_X.flatten()}")