import pandas as pd
import numpy as np

file = pd.read_excel(r"Lab Session1 Data.xlsx",sheet_name="Purchase data")
A = file[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C = file['Payment (Rs)'].to_numpy().reshape(-1, 1)
print(f"A = {A}")
print(f"C = {C}")

dimensionality = A.shape[1]
print("the dimensionality of the vector space is  = " + str(dimensionality))

vector_space = A.shape[0]
print("the number of vectors in the vector space is = " + str(vector_space))

rank_A = np.linalg.matrix_rank(A)
print("the rank of the matrix  A is = " + str(rank_A))

pseudo_inverse = np.linalg.pinv(A)
print("the pseudo inverse of matrix A is = " + str(pseudo_inverse))

cost = np.dot(pseudo_inverse,C)
print("the cost of each product that is available for sale is  = " + str(cost.flatten()))

