import pandas as pd 
import plotly.express as px

data = pd.read_csv("DailyDelhiClimateTest.csv")

figure = px.line(data, x= "date", y = "meantemp", title="Mean Temperature in Delhi Over the Years")
figure.show()