import streamlit as st
import PyPDF2
import re

st.title("Zambia Mining Audit: Policy Insights")

uploaded_file = st.file_uploader("Upload the Amendment Act", type="pdf")

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = " ".join([page.extract_text() or "" for page in reader.pages])

    st.subheader("📊 Policy Breakdown")

    # Insight 1: Copper Pricing Tiers
    if "copper" in text.lower():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Low Tier", "4%", "Price < $4,500")
        with col2:
            st.metric("Mid Tier", "5%", "$4,500 - $6,000")
        with col3:
            st.metric("High Tier", "6%", "Price > $6,000")
        st.info("💡 Insight: Zambia uses a sliding scale for copper. This is designed to capture more revenue when global prices are high.")

    # Insight 2: High-Value Minerals
    precious = re.findall(r'(precious metals|gemstones).{1,50}(six percent|6%)', text, re.IGNORECASE)
    if precious:
        st.warning("💎 High-Value Resource Flag: Precious metals and gemstones are taxed at a flat 6%.")

    # Insight 3: The 'Activist' Check (Transparency)
    if "Commissioner-General" in text:
        st.write("### ⚖️ Accountability Note")
        st.write("The Act gives the **Commissioner-General** power to adjust values if they don't match 'arm's length' transactions. This is a key tool against tax avoidance by mining companies.")