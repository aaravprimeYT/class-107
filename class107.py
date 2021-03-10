import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("class107.csv")

mean = df.groupby("level")["attempt"].mean()
print(mean)

fig = go.Figure(go.Bar(x = mean, y = ["Level 1","Level 2","Level 3","Level 4"], orientation = "h"))
fig.show()