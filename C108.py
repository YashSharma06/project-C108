import csv
import pandas as pd
import plotly.figure_factory as ff

cd = pd.read_csv("data108.csv")

fig = ff.create_distplot([cd["Avg Rating"].tolist()],["Brand"], show_hist = False)

fig.show()
