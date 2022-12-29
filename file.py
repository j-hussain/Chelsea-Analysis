import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')

st.write("Here's some data!")
st.write(df)