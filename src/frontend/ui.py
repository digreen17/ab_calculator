
import streamlit as st
st.set_page_config(page_title="AB Calculator", layout="wide")

sample_size  = st.Page("streamlit_pages/calculate_sample_size.py", title="Sample size")
about = st.Page("streamlit_pages/about.py",      title="О проекте")

current = st.navigation([about, sample_size], position="sidebar")   
