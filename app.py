import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# STAGE 1: UI INITIALIZATION (MATCHING SCREENSHOT 11:16:42)
st.set_page_config(page_title="Music Anomaly Hub", layout="wide", initial_sidebar_state="expanded")
st.title("🎵 Music Anomaly Hub: Sovereign Operator")

try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # STAGE 2: FORMULA INJECTION (S = R/P)
    # Market Score favors low views (P) and high staleness/gap
    df['Market Score'] = (df['Gap Score'] * df['Staleness (yrs)']) / (np.log1p(df['Top Video Views (K)']) + 1)

    # STAGE 3: TABS (EXACT RECOVERY)
    tab1, tab2, tab3 = st.tabs(["🔍 Gap Scanner", "📊 Market Graph", "🛠 Metadata Architect"])

    with tab1:
        st.sidebar.header("Scan Parameters")
        search = st.sidebar.text_input("Niche Keywords", "working from home")
        min_gap = st.sidebar.slider("Min Gap Score", 0, 100, 60)
        
        # RESTORING THE ORANGE BUTTON (SCREENSHOT 11:16:42)
        st.markdown("""<style>div.stButton > button:first-child { background-color: #FF8C00; color: white; }</style>""", unsafe_allow_html=True)
        if st.button("🟠 RUN GAP SCAN", use_container_width=True):
            results = df[(df['Keyword'].str.contains(search, case=False)) & (df['Gap Score'] >= min_gap)]
            results = results.sort_values(by='Market Score', ascending=False)
            
            # DETECTED ALERTS (SCREENSHOT 11:20:19)
            st.warning(f"⚠️ SYSTEM ALERT: Detected {len(results)} Potential Anomalies in '{search}'")
            st.dataframe(results, use_container_width=True, hide_index=True)
        else:
            st.info("Awaiting Operator Input: Adjust parameters and click 'RUN GAP SCAN'")

    with tab2:
        st.subheader("Anomaly Density Visualization")
        # RESTORING THE GRAPH (SCREENSHOT 11:19:57)
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df, x='Gap Score', y='Staleness (yrs)', size='Top Video Views (K)', hue='Market Score', palette='viridis', ax=ax)
        st.pyplot(fig)

    with tab3:
        # RESTORING METADATA & SEO (SCREENSHOT 11:30:54 / 11:31:08)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Utility Profile Generator")
            if st.button("GENERATE FULL UTILITY PROFILE"):
                st.success("Utility Profile Synchronized.")
                st.write("**Target Duration:** 120 Minutes")
                st.write("**Key Prompt:** [Scholarly Noir] [Focus: Rain on Glass]")
        
        with col2:
            st.subheader("YouTube SEO Architecture")
            # RESTORING TEXT AREAS (SCREENSHOT 11:31:08)
            st.text_area("Title Architecture", f"2026 DEEP FOCUS: 2-Hour {search} (No Vocals)", height=100)
            st.text_area("Tags / Metadata", f"{search}, Focus Music 2026, Academic Noir, Scholarly Noir", height=100)

except Exception as e:
    st.error(f"FATAL SYSTEM ERROR: {e}. Ensure 2026-05-04T15-20_export.csv is in root.")
