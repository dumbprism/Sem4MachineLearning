import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')


file.dropna(subset=['Instructions'], inplace=True)


instructions = file['Instructions']

# Tokenize instructions by word count
instruction_lengths = instructions.str.split().apply(len)

# Calculate mean and variance
mean_instruction_length = instruction_lengths.mean()
variance_instruction_length = instruction_lengths.var()

print("Mean instruction length:", mean_instruction_length)
print("Variance of instruction length:", variance_instruction_length)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(instruction_lengths, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Instruction Lengths')
plt.xlabel('Number of Words')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
