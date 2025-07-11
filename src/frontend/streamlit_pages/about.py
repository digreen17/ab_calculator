import streamlit as st
import pandas as pd

st.set_page_config(page_title="About", layout="centered")

st.title("About")

left, right = st.columns(2)
with left:
    st.subheader("Repository")
    st.write("[AB Calculator on GitHub](https://github.com/digreen17/ab_calculator)")

with right:
    st.subheader("Contact")
    st.write("[LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("[Telegram](https://t.me/digreen_17)")

st.divider()

st.subheader("Sample‑Size Calculator")
st.write("Determines the minimum number of observations required per experimental group.")

core_params = pd.DataFrame(
    {
        "Parameter": [
            "Metric type",
            "MDE (%)",
            "Power (1−β)",
            "Alpha (α)",
        ],
        "Purpose": [
            "continuous or binary metric",
            "Minimum detectable effect",
            "Probability of detecting a true effect",
            "Significance level",
        ],
    }
)

st.write("#### Core parameters")
st.table(core_params.set_index(core_params.columns[0]))

st.write("#### Additional parameters")
continuous_tab, binary_tab = st.tabs(["Continuous metric", "Binary metric"])

with continuous_tab:
    continuous_params = pd.DataFrame(
        {
            "Parameter": [
                "Mean",
                "Standard deviation",
                "Data is skewed?",
            ],
            "Purpose": [
                "Expected average value",
                "Expected variability",
                "Apply variance‑stabilising correction",
            ],
        }
    )
    st.table(continuous_params.set_index(continuous_params.columns[0]))

with binary_tab:
    binary_params = pd.DataFrame(
        {
            "Parameter": ["p"],
            "Purpose": ["Baseline success probability"],
        }
    )
    st.table(binary_params.set_index(binary_params.columns[0]))

st.info("After entering the parameters, the calculator outputs the minimum sample size per group.")
