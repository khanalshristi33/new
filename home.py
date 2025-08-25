import streamlit as st
import pandas as pd
import seaborn as sns

st.header("WELCOME TO ANALYSIS OF VIDEO GAMING SALES DATA")
df = pd.read_csv('GRAPH/PS4_GamesSales.csv')