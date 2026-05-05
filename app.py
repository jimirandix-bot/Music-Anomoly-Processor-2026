import streamlit as st
import pandas as pd

# UI Architecture
st.set_page_config(page_title="Anomaly Gap Finder v2", layout="wide")
st.title("🎵 Anomaly Gap Finder: Sovereign Operator v2")

# Logic: S = R/P (Results = Retention / Perception)
# P-Reduction Filter: Removes high-density market nodes.

try:
    # Payload Injection
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # Apply V2 Density Filter (Max 100k Views to beat)
    v2_vacuums = df[
        (df['Gap Score'] > 65) & 
        (df['Top Video Views (K)'] < 100)
    ].sort_values(by='Staleness (yrs)', ascending=False)

    st.subheader("🚀 High-Value Vacuums: Low Competition Nodes")
    st.dataframe(v2_vacuums)
    
    # Strategy Directive
    st.sidebar.header("Current Directive")
    st.sidebar.success("Target: Background music for working from home")
    st.sidebar.info("Metric: P < 100k Views. Status: OPTIMAL.")

except Exception as e:
    st.error(f"Waiting for CSV integrity check: {e}")
