from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.gapminder()


countries = pd.Series(df["country"]).unique()

# Initialize Dash App
app = Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="country-dropdown",
            options=[{"label": c_name, "value": c_name} for c_name in countries],
            value="Canada",
        ),
        dcc.Graph(id="gdp-growth"),
    ]
)


@app.callback(Output("gdp-growth", "figure"), [Input("country-dropdown", "value")])
def update_graph(c_name):
    data = df[df["country"] == c_name]
    fig = px.line(
        data, x="year", y="gdpPercap", title=f"GDP Per Capita Over Time: {c_name}"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
