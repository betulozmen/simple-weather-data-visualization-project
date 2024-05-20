import pandas as pd
import plotly.express as px

data = pd.read_csv("DailyDelhiClimateTest.csv")

figure = px.line(data, x="date", y="wind_speed", title="Wind Speed in Delhi Over yhe Years")
figure.show()