import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Music Anomaly Hub", layout="wide")
st.title("🎵 Music Anomaly Hub: Sovereign Operator v2")

try:
    df = pd.read_csv('2026-05-04T15-20_export.csv')
    
    # Formula: V2 Saturation Penalty
    df['Adjusted Score'] = df['Gap Score'] * (1 / (np.log1p(df['Top Video Views (K)']) + 1))

    # TABS: ORIGINAL DNA
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Gap Scanner", "📊 Market Graph", "🛠 Metadata Architect", "📝 YouTube SEO"])

    with tab1:
        st.sidebar.header("Scan Parameters")
        search = st.sidebar.text_input("Niche Keywords", "working from home")
        run_scan = st.button("🟠 RUN GAP SCAN", use_container_width=True)
        
        if run_scan or search:
            results = df[df['Keyword'].str.contains(search, case=False)].sort_values(by='Adjusted Score', ascending=False)
            st.warning(f"⚠️ SYSTEM ALERT: Detected {len(results)} Potential Anomalies")
            st.dataframe(results, use_container_width=True)
        else:
            st.info("System Standby: Awaiting Scan Initiation.")

    with tab2:
        st.subheader("Anomaly Density Visualization")
        if not df.empty:
            fig, ax = plt.subplots()
            sns.scatterplot(data=df, x='Gap Score', y='Staleness (yrs)', size='Top Video Views (K)', hue='Adjusted Score', ax=ax)
            st.pyplot(fig)

    with tab3:
        st.subheader("Utility Profile Generator")
        if st.button("GENERATE FULL UTILITY PROFILE"):
            st.success("Generating lossless prompt architecture for Sonauto...")
            st.code(f"PROMPT: [120 Minutes] [Academic Noir] [Focus: {search}]")

    with tab4:
        st.subheader("YouTube SEO Architecture")
        st.text_area("Title Architecture", f"2026 DEEP FOCUS: 2-Hour {search} (No Vocals)")
        st.text_area("Tags / Metadata", f"{search}, Focus Music 2026, Academic Noir, Study Music")

except Exception as e:
    st.error(f"FATAL SYNC ERROR: {e}")
