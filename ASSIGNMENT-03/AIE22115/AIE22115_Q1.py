import pandas as pd
import numpy as np

# read the excel file
file = pd.read_excel(r"C:\Users\navee\Downloads\Lab Session1 Data.xlsx",sheet_name="Purchase data")
A = file[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C = file['Payment (Rs)'].to_numpy().reshape(-1, 1)

# display the matrix A and C
print(f"A = {A}")
print(f"C = {C}")

# print the dimensionality of the vector space
dimensionality_vectorspace = A.shape[1]
print("Dimensionality of vector space is = " + str(dimensionality_vectorspace))

# print the number of vectors in vectors in vector space
vectors_vectorspace = A.shape[0]
print("NO of vectors in vectors space is = " + str(vectors_vectorspace))

# print the rank of rank A
rank_matrix_A = np.linalg.matrix_rank(A)
print("Rank of matrix A is = " + str(rank_matrix_A))

# print the pseudo inverse of matrix A
pseudo_inverse_A = np.linalg.pinv(A)
print("pseudo inverse is= " + str(pseudo_inverse_A))

# print the cost of each product using the pseudo inverse
cost = np.dot(pseudo_inverse_A,C)
print("cost of each product that is available for sale is  = " + str(cost.flatten()))