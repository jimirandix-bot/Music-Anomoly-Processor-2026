import streamlit as st
import pandas as pd

# UI CONFIGURATION
st.set_page_config(page_title="Anomaly Gap Finder v2", layout="wide")
st.title("🎵 Anomaly Gap Finder: Sovereign Hub")

# SIDEBAR: STRATEGIC DIRECTIVE
st.sidebar.header("Operator Status")
st.sidebar.success("V2 Density Filter: ACTIVE")
st.sidebar.info("Target: 'Work From Home' Niche")

# DATA INJECTION
try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # UI TABS RESTORATION
    tab1, tab2, tab3 = st.tabs(["🚀 Market Vacuums", "📊 Data Audit", "🛠 System Strategy"])

    with tab1:
        st.subheader("High-Value / Low-Density Nodes")
        # Apply V2 Density Filter (Max 100k Views)
        v2_vacuums = df[
            (df['Gap Score'] > 65) & 
            (df['Top Video Views (K)'] < 100)
        ].sort_values(by='Staleness (yrs)', ascending=False)
        st.dataframe(v2_vacuums, use_container_width=True)

    with tab2:
        st.subheader("Raw Market Export")
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("Execution Logic: S = R/P")
        st.write("1. **R (Retention):** 120-Minute Sonauto Build.")
        st.write("2. **P (Perception/Competition):** Targeting nodes < 100k views.")
        st.write("3. **Status:** Move to Sonauto for 'Work From Home' asset.")

except Exception as e:
    st.error(f"Integrity Sync Failed: {e}")
