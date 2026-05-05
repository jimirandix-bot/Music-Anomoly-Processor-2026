import streamlit as st
import pandas as pd

st.set_page_config(page_title="Music Anomaly Hub", layout="wide")
st.title("🎵 Music Anomaly Hub: Strategy Dashboard")

# Core Data Engine
try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    st.subheader("Live Market Gaps (Gap Score > 65)")
    # Pivot to Work From Home Niche
    filtered_df = df[df['Gap Score'] > 65].sort_values(by='Staleness (yrs)', ascending=False)
    st.dataframe(filtered_df)
    
    st.success("Target: Background music for working from home (78k Competition)")
except Exception as e:
    st.error(f"Waiting for CSV synchronization: {e}")
