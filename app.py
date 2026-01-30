import streamlit as st
import PyPDF2
import re

st.title("🇿🇲 Zambian Mining Fiscal Policy Visualizer: Technical Summarization")

uploaded_file = st.file_uploader("Upload a Mining Act", type="pdf")

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = " ".join([page.extract_text() or "" for page in reader.pages])

    # 1. Version Detection
    is_2016 = "2016" in text and "Amendment" in text
    is_2015 = "2015" in text and not is_2016
    st.subheader("📊 Policy Breakdown")

    # Insight 1: Copper Pricing Tiers
    if is_2016:
        st.info("📂 Detected: Mines and Minerals Development (Amendment) Act, 2016")
        # Apply the sliding scale logic
        st.write("### 📊 2016 Variable Royalty Structure (Copper)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Low Tier", "4%", "< $4,500")
        col2.metric("Mid Tier", "5%", "$4,500 - $6,000")
        col3.metric("High Tier", "6%", "> $6,000")
    elif is_2015:
        st.info("📂 Detected: Mines and Minerals Development Act, 2015")
        st.write("### 📊 2015 Fixed Royalty Structure")
        st.warning("Note: The 2015 Act initially set higher flat rates (e.g., 9% for open-cast) before the 2016 amendment.")
        # Regex to find any flat 'percent' mentions in the 2015 text
        flat_rates = re.findall(r'(\d+)\s*percent', text)
        st.write(f"Detected Flat Rates: {set(flat_rates)}")
    else:
        st.warning("Unknown Document Version. Proceeding with general text extraction.")
        
    # Insight 2: High-Value Minerals
    precious = re.findall(r'(precious metals|gemstones).{1,50}(six percent|6%)', text, re.IGNORECASE)
    if precious:
        st.warning("💎 High-Value Resource Flag: Precious metals and gemstones are taxed at a flat 6%.")

    # Insight 3: The 'Activist' Check (Transparency)
    if "Commissioner-General" in text:
        st.write("### ⚖️ Accountability Note")
        st.write("The Act gives the **Commissioner-General** power to adjust values if they don't match 'arm's length' transactions. This is a key tool against tax avoidance by mining companies.")