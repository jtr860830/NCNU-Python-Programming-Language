import csv
import requests

import pandas as pd
from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot

URL: str = "https://www.twse.com.tw/exchangeReport/FMSRFK?response=json&date=20221116&stockNo=2603&_=1668598936075"
PATH: str = "./twse_2603.csv"

res: dict = requests.get(URL).json()
with open(PATH, "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(res["fields"])
    csv_writer.writerows(res["data"])

data = pd.read_csv(PATH, encoding="utf-8")

graph: list[Scatter] = [
    Scatter(x=data["月份"], y=data["最高價"], name="最高價"),
    Scatter(x=data["月份"], y=data["最低價"], name="最低價"),
]

plot({"data": graph, "layout": Layout(title="s111213515_h1")}, auto_open=True)
