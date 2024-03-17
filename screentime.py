import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go 
data=pd.read_csv("Screentime-App-Details.csv")
print(data.head())
data.isnull().sum()
print(data.describe())
figure=px.bar(data_frame=data,
              x="Date",
              y="Usage",
              color="app",
              title="Usage")
figure.show()
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()
figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()
figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()