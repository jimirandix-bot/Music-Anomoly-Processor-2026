import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# UI INITIALIZATION (EXACT SCREENSHOT MATCH)
st.set_page_config(page_title="Music Anomaly Hub", layout="wide")
st.title("🎵 Music Anomaly Hub: Sovereign Operator")

try:
    # DATA INJECTION
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # FORMULA: SATURATION PENALTY (V2 LOGIC)
    df['Market Score'] = (df['Gap Score'] * df['Staleness (yrs)']) / (np.log1p(df['Top Video Views (K)']) + 1)

    # TABS: FULL RESTORATION
    tab1, tab2, tab3 = st.tabs(["🔍 Gap Scanner", "📊 Market Graph", "🛠 Metadata Architect"])

    with tab1:
        st.sidebar.header("Scan Parameters")
        search = st.sidebar.text_input("Niche Keywords", "working from home")
        min_gap = st.sidebar.slider("Min Gap Score", 0, 100, 60)
        
        # CSS FOR ORANGE BUTTON (SCREENSHOT 11:16:42)
        st.markdown("""<style>div.stButton > button:first-child { background-color: #FF8C00 !important; color: white !important; }</style>""", unsafe_allow_html=True)
        
        if st.button("🟠 RUN GAP SCAN", use_container_width=True):
            results = df[df['Keyword'].str.contains(search, case=False)].sort_values(by='Market Score', ascending=False)
            st.warning(f"⚠️ SYSTEM ALERT: Detected {len(results)} Potential Anomalies")
            st.dataframe(results, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Anomaly Density Visualization")
        # GRAPH RESTORATION (SCREENSHOT 11:19:57)
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df, x='Gap Score', y='Staleness (yrs)', size='Top Video Views (K)', hue='Market Score', palette='flare', ax=ax)
        st.pyplot(fig)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Utility Profile Generator")
            if st.button("GENERATE FULL UTILITY PROFILE"):
                st.success("Utility Profile Synchronized.")
                st.write("**Target:** 120-Minute Audio Asset")
                st.write("**Prompt:** [Scholarly Noir] [Metronomic Pulse]")
        
        with col2:
            st.subheader("YouTube SEO Architecture")
            # SEO TEXT AREAS (SCREENSHOT 11:31:08)
            st.text_area("Title Architecture", f"2026 DEEP FOCUS: 2-Hour {search} (No Vocals)", height=100)
            st.text_area("Tags / Metadata", f"{search}, Focus Music 2026, Academic Noir, Study Music", height=100)

except Exception as e:
    st.error(f"DEPLOYMENT ERROR: Ensure 'requirements.txt' is created in GitHub. Details: {e}")
