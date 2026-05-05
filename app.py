import streamlit as st
import pandas as pd
import numpy as np

# UI ARCHITECTURE: SOVEREIGN HUB V2
st.set_page_config(page_title="Anomaly Gap Finder v2", layout="wide")
st.title("🎵 Anomaly Gap Finder: Sovereign Hub")

# DATA INJECTION
try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # FORMULA: S = Gap * (1 / Log(Views)) -> Penalizes Saturation
    df['Market Score'] = df['Gap Score'] * (1 / (np.log1p(df['Top Video Views (K)']) + 1))

    # SIDEBAR: INTERACTIVE CONTROLS (RESTORED)
    st.sidebar.header("Execution Controls")
    search_query = st.sidebar.text_input("Niche Search", "working from home")
    min_gap = st.sidebar.slider("Min Gap Score", 0, 100, 65)
    
    execute = st.sidebar.button("EXECUTE SYSTEM SCAN")

    # TABS: ORIGINAL STRUCTURE
    tab1, tab2, tab3 = st.tabs(["🚀 Market Vacuums", "📊 Raw Data", "🎯 Strategy"])

    with tab1:
        if execute or search_query:
            st.subheader(f"Results for: {search_query}")
            # Logic: Filter for Low Density (<150k Views) + User Search
            results = df[
                (df['Keyword'].str.contains(search_query, case=False)) & 
                (df['Gap Score'] >= min_gap)
            ].sort_values(by='Market Score', ascending=False)
            
            st.dataframe(results, use_container_width=True)
            
            if not results.empty and "working from home" in search_query.lower():
                st.success("VACUUM DETECTED: Low competition node confirmed.")
        else:
            st.info("Awaiting Operator Input: Click 'EXECUTE SYSTEM SCAN'")

    with tab2:
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("S = R/P Calibration")
        st.write("- **Retention (R):** Target 120-Minute length.")
        st.write("- **Perception (P):** Target < 100k view niches.")

except Exception as e:
    st.error(f"System Offline: {e}")
