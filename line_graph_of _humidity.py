import pandas as pd
import plotly.express as px

data = pd.read_csv("DailyDelhiClimateTest.csv")

figure = px.line(data, x="date", y="humidity", title="Humidity in Delhi Over the Years")
figure.show()