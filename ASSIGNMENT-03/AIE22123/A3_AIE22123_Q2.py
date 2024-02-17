import pandas as pd
import numpy as np

file = pd.read_excel(r"Lab Session1 Data.xlsx",sheet_name="Purchase data")
A = file[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C = file['Payment (Rs)'].to_numpy().reshape(-1, 1)
print(f"A = {A}")
print(f"C = {C}")

#finding the pseudo inverse
pseudo_inverse = np.linalg.pinv(A)

model_vector_X = np.dot(pseudo_inverse,C)
print(f"The model vector X for predicting the cost of the products available with the vendor = {model_vector_X.flatten()}")
