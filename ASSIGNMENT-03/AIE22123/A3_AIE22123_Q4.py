import statistics
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
import seaborn as sns
import math

file = pd.read_excel(r"Lab Session1 Data.xlsx" , sheet_name="IRCTC Stock Price")

column_D = file.iloc[: , 3]
print(f"D = {column_D}")

mean  = statistics.mean(column_D)
print(f"the mean of column D is = {mean}")

variance = statistics.variance(column_D)
print(f"the variance of column D is = {variance}")


file["Date"] = pd.to_datetime(file["Date"])
file["weekday"] = file["Date"].dt.weekday
wednesdays = file[file['weekday'] == 2]
wednesdays_price = wednesdays['Price']
wednesday_mean = wednesdays_price.mean()

print(f"The sample mean of for all Wednesdays in the dataset is  = {wednesday_mean}")


file['Month'] = file["Date"].dt.month
April_data = file[file["Month"]==4]
April_mean = statistics.mean(April_data['Price'])

print(f"The sample mean of for April in the dataset is  = {April_mean}")


loss = lambda x:x<0 
loss_count = (file['Chg%'] <0).sum()
total = len(file)
probablity = loss_count/total

print(f"the probability of making loss in the stock is {probablity}")

profit = lambda x:x>0
profit_count = (file.loc[file['weekday'] == 2 , 'Chg%'] > 0).sum()
probablity_wed = profit_count/total

print(f"the probability of making profit in the stock on wednesday is {probablity_wed}")

profit_wednesday = wednesdays[wednesdays['Chg%'] > 0]
num_profit_wednesdays = len(profit_wednesday)
total_wed = len(wednesdays)
conditional_prob_wed = num_profit_wednesdays/total_wed
print(f"The cnditional probablity of making profit, given that today is wednesday = {conditional_prob_wed}")

file["Day_of_week"] = file['Date'].dt.weekday
sns.scatterplot(x="Day_of_week", y="Chg%", data=file, hue="Day_of_week", palette="hls")
plt.xlabel("Day(of the week)")
plt.ylabel("Chg%")
plt.title("Chg% Distribution against the day of the week")
plt.show()