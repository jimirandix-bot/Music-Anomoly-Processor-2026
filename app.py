import streamlit as st
import pandas as pd

st.title("🎵 Music Anomaly Hub")
st.write("Target: Background music for working from home (Gap: 68.88)")

try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    st.dataframe(df[df['Gap Score'] > 65])
except:
    st.error("Missing CSV file in repository.")
