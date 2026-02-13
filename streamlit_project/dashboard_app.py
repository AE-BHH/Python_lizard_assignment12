import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np

# Create sample data — just faking some numbers to simulate a small product dataset

np.random.seed(42)  # Setting a seed so results are consistent every time you run
sample_data = {
    "Product": ["Product A", "Product B", "Product C", "Product D"],
    "Sales": np.random.randint(100, 500, size=4),  # Random sales numbers
    "Profit": np.random.randint(20, 100, size=4),  # Random profit numbers
}
df = pd.DataFrame(sample_data)

# Sidebar filters — this shows up in the sidebar for user interaction

st.sidebar.header("Filter Options")  # Sidebar title
selected_product = st.sidebar.selectbox(
    "Select Product", df["Product"]
)  # Dropdown to choose a product


# Filter the data based on the user's selection
filtered_df = df[df["Product"] == selected_product]

# Main app content starts here
st.title("Simple Product Dashboard")  # Big title for the dashboard

# Display key numbers using metrics — side-by-side using columns
col1, col2 = st.columns(2)
with col1:
    st.metric("Sales", f"${filtered_df['Sales'].values[0]:,}")

with col1:
    st.metric("Profit", f"${filtered_df['Profit'].values[0]:,}")


st.subheader("Sales and Profit Comparison")
bar_chart = px.bar(df, x="Product", y=["Sales", "Profit"], barmode="group")
st.plotly_chart(bar_chart)
