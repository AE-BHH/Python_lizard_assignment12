import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect("../db/lesson.db")
cur = conn.cursor()
print("Connected to DB.")

query = "SELECT o.order_id, sum(p.price * li.quantity) AS total_price FROM orders o JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id GROUP BY o.order_id;"

# cur.execute(query)
# print(cur.fetchall())

df = pd.read_sql_query(query, conn)
print(df)


def cumulative(row):
    totals_above = df["total_price"][0 : row.name + 1]
    return totals_above.sum()


df["cumulative"] = df.apply(cumulative, axis=1)
print(df.head())

df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    grid=True,
    title="Cumulative Revenue Based On Order ID",
)
plt.show()
