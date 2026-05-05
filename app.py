import streamlit as st
import pandas as pd
import numpy as np

# UI ARCHITECTURE: SOVEREIGN HUB
st.set_page_config(page_title="Anomaly Gap Finder v2", layout="wide")
st.title("🎵 Anomaly Gap Finder: Sovereign Hub")

# DATA INJECTION
try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # FORMULA CALIBRATION: SATURATION PENALTY
    # We penalize high views (Saturation) and favor low views (Vacuums)
    df['Market Adjusted Score'] = df['Gap Score'] * (1 / (np.log1p(df['Top Video Views (K)']) + 1))
    
    # SIDEBAR: STRATEGIC DIRECTIVE
    st.sidebar.header("Operator Status")
    st.sidebar.success("V2 Saturation Filter: ACTIVE")
    target_row = df.loc[df['Keyword'].str.contains("working from home", case=False)].iloc[0]
    st.sidebar.metric("Target Density", f"{target_row['Top Video Views (K)']}K")

    # TABS: ORIGINAL STRUCTURE RESTORED
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 Market Vacuums", "📊 Data Audit", "🎯 Strategy", "🛠 Metadata"])

    with tab1:
        st.subheader("High-Value / Low-Density Vacuums")
        # Filter: High Gap + Low Competition
        v2_vacuums = df[df['Top Video Views (K)'] < 150].sort_values(by='Market Adjusted Score', ascending=False)
        st.dataframe(v2_vacuums, use_container_width=True)

    with tab2:
        st.subheader("Raw Market Export")
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("The S = R/P Pivot")
        st.info("Study Music (P = 58M) = METABOLIC LEAKAGE. Avoid.")
        st.success("Work From Home (P = 78K) = SYSTEM SUCCESS. Execute.")
        
    with tab4:
        st.subheader("2026 Asset Anchoring")
        st.code(f"Title: 2026 DEEP FOCUS: 2-Hour {target_row['Keyword']}")
        st.code("Tags: Work from home, Focus music 2026, Academic Noir")

except Exception as e:
    st.error(f"Integrity Sync Failed: {e}")
