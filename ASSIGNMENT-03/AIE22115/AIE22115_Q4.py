import statistics
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns

data_set = pd.read_excel(r"C:\Users\navee\Downloads\Lab Session1 Data.xlsx", sheet_name="IRCTC Stock Price")
 
col_D = data_set.iloc[:,3]
stat_mean = statistics.mean(col_D)
stat_var = statistics.variance(col_D)

data_set["Date"] = pd.to_datetime(data_set["Date"])
data_set['weekday'] = data_set["Date"].dt.weekday
wednesdays = data_set[data_set['weekday'] == 2]
wednesdays_price = wednesdays['Price']
wednesday_mean = wednesdays_price.mean()

data_set['Month'] = data_set["Date"].dt.month
april_data = data_set[data_set["Month"]==4]
April_mean = statistics.mean(april_data['Price'])

is_loss = lambda x:x<0 
loss_count = data_set['Chg%'].apply(is_loss).sum()
total_count = len(data_set)
probability_of_loss = loss_count/total_count

is_profit = lambda x:x>0
profit_count = data_set[data_set['weekday'] == 2]['Chg%'].apply(is_profit).sum()
probability_of_wed_profit = profit_count/total_count

profitable_wednesday = wednesdays[wednesdays['Chg%'] > 0]
num_profitable_wednesdays = len(profitable_wednesday)
total_wed = len(wednesdays)
conditional_prob_wed = num_profitable_wednesdays/total_wed

data_set["Day_of_week"] = data_set['Date'].dt.weekday
sns.scatterplot(x="Day_of_week", y="Chg%", data=data_set, hue="Day_of_week", palette="hls")
plt.xlabel("Day of the Week")
plt.ylabel("Chg%")
plt.title("Chg% Distribution by Day of the Week")
plt.show()

print(f"mean of wednesday is {wednesday_mean}")
print(f"mean of dataset is {stat_mean}")
print(f"variance of the dataset is {stat_var}")
print(f"mean of the April month is {April_mean}")
print(f"probability Making the loss of the stock {probability_of_loss}")
print(f"probability of profit making on wednesday is {probability_of_wed_profit}")
print(f"conditional probability of making profit that given date is wednesday is : {conditional_prob_wed}")