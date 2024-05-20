import pandas as pd
import plotly.express as px

data = pd.read_csv("DailyDelhiClimateTest.csv")

figure = px.scatter(data_frame=data, x="humidity", y="meantemp", size="meantemp", trendline="ols", title="Relationship Between Temperature and Humidity")
figure.show()