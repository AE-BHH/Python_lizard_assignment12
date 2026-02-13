import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Expenses": [80, 120, 180, 200, 220, 300],
}

df = pd.DataFrame(data)

# Line Plot
df.plot(
    x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs Expenses", grid=0.5
)
plt.show()

# Bar Plot
df.plot(x="Month", y="Sales", kind="bar", color="Skyblue", title="Monthly Sales")
plt.show()
