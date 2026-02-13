import streamlit as st

# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple TEXT")  # Displays plain, unformatted text — like a basic message
st.markdown(
    "**Bold** & *italic* text"
)  # Markdown lets you add simple formatting like bold and italics


st.write("Automatic data display")
st.code("print('Hello World!)", language="python")
st.latex(r"\int_{a}^{b} x^2 dx")

# Exercise - 2: Data Input Components

st.header("Section 2")
name = st.text_input("Enter your name here ....")
last_name = st.text_input("Enter your last name here ....")

description = st.text_area("Write your message here ...")

age = st.number_input("Age", min_value=0, max_value=120, value=30)

score = st.slider("Score", 0, 100, 50)

option = st.selectbox("Choose an option", ["A", "B", "C"])

options = st.multiselect("Multiple Options", ["X", "Y", "Z"])

date = st.date_input("Select date")
time = st.time_input("Select time")

if st.button("Click me"):
    st.write("Button clicked")

if st.checkbox("Show/Hide"):
    st.write("visible content")


# Exercise 3: Layout and Containers

st.header("Section 3")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")


with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with st.expander("Click to expand"):
    st.write("Expanded content here")


st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select Option", ["A", "B", "C"])
