import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("DailyDelhiClimateTest.csv")

data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
data["year"] = data["date"].dt.year
data['month'] = data["date"].dt.month
data['day'] = data["date"].dt.day
print(data.head())

plt.style.use('fivethirtyeight')
plt.figure(figsize=(10, 7))
plt.title("Temperature Change in Delhi Over the Years")
sns.lineplot(data=data,x='month', y='meantemp', hue='year')
plt.show()