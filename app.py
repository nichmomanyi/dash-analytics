from dash import Dash, dcc, html
import pandas as pd

data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region ='Albany'")
data["Date"] = pd.to_datetime(data["Date"], format = "%Y-%m-%d")

data.sort_values("Date", inplace=True)

app = Dash(__name__ )

app.layout =html.Div(
    children = [
        html.H1(children = "Avocado Analytics"),
        html.P(children = "Analyze the behavior of Avocado prices"
                " and the number of avocado sold in the USA"
                "between 2015 and 2018"),
        dcc.Graph(
            figure = {
                "data": [
                { 
                "x": data["Date"],
                "y": data["AveragePrice"],
                "type": "line"
                },
                ],
                "layout": {"title": "Average Avocado Prices"}
            },
        ),
        dcc.Graph(
            figure = {
                "data": [
                { 
                "x": data["Date"],
                "y": data["Total Volume"],
                "type": "line"
                },
                ],
                "layout": {"title": "Total Avocado Volume Sold"}
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)