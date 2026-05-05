import streamlit as st
import pandas as pd
import numpy as np

# UI ARCHITECTURE: SOVEREIGN HUB V2.1
st.set_page_config(page_title="Anomaly Gap Finder", layout="wide")
st.title("🎵 Anomaly Gap Finder: Sovereign Hub")

# DATA INJECTION
try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # V2 FORMULA: CALCULATE MARKET STRENGTH (Penalize Saturation)
    df['Market Score'] = (df['Gap Score'] * df['Staleness (yrs)']) / (np.log1p(df['Top Video Views (K)']) + 1)

    # SIDEBAR: INTERACTIVE SEARCH (LIVE)
    st.sidebar.header("System Controls")
    query = st.sidebar.text_input("Niche Search", value="working from home")
    threshold = st.sidebar.slider("Min Gap Score", 0, 100, 60)

    # TABS: ORIGINAL MULTI-TAB ARCHITECTURE
    tab1, tab2, tab3 = st.tabs(["🚀 Market Vacuums", "📊 Data Audit", "🎯 Execution Strategy"])

    with tab1:
        st.subheader(f"Optimal Entry Points: {query}")
        
        # Live Filter Logic
        mask = (df['Keyword'].str.contains(query, case=False)) & (df['Gap Score'] >= threshold)
        filtered_df = df[mask].sort_values(by='Market Score', ascending=False)

        # COLUMN FIX: Automated Width & Scannability
        st.dataframe(
            filtered_df,
            column_config={
                "Keyword": st.column_config.TextColumn("Keyword", width="medium"),
                "Top Video Title": st.column_config.TextColumn("Top Video Title", width="large"),
                "Gap Score": st.column_config.NumberColumn("Gap", format="%d"),
            },
            use_container_width=True,
            hide_index=True
        )

    with tab2:
        st.subheader("Raw Data Ledger")
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("Strategy: S = R/P")
        st.info("Target Detected: 'Work From Home' has lowest Density (P).")
        st.success("Directive: 120-Minute Render Required.")

except Exception as e:
    st.error(f"System Offline: {e}")
