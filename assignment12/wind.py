import plotly.data as pldata
import plotly.express as px
import matplotlib.pylab as plt
import pandas as pd


df = pldata.wind(return_type="pandas")
print(df.head(10))
print(df.tail(10))

print(df["strength"].unique())
df["strength"] = df["strength"].str.replace(r"[^0-9.]", "", regex=True)
print(df.head(10))
df["strength"] = df["strength"].astype(float)
print(df.head(10))

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency",
    hover_data="frequency",
)
fig.write_html("wind.html", auto_open=True)
