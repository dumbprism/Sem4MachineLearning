import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

file_path = r"Lab Session1 Data.xlsx"
df = pd.read_excel(file_path, sheet_name="Purchase data")

print("All Column Names:", df.columns)

actual_prices_column_name = 'Milk'
predicted_prices_column_name = 'Milk'

actual_prices = df[actual_prices_column_name].values
predicted_prices = df[predicted_prices_column_name].values

df_cleaned = df.dropna(subset=[actual_prices_column_name, predicted_prices_column_name])

actual_prices = df_cleaned[actual_prices_column_name].values
predicted_prices = df_cleaned[predicted_prices_column_name].values

print("Actual Values:", actual_prices)
print("Predicted Values:", predicted_prices)

mse = mean_squared_error(actual_prices, predicted_prices)

rmse = np.sqrt(mse)

mape = np.mean(np.abs((actual_prices - predicted_prices) / actual_prices)) * 100

if len(actual_prices) >= 2:
    r2 = r2_score(actual_prices, predicted_prices)
    print(f'R-squared (R2) score: {r2}')
else:
    print('Insufficient samples to calculate R-squared.')

print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'Mean Absolute Percentage Error (MAPE): {mape}')