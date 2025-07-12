import pandas as pd
import streamlit as st

st.set_page_config(page_title="About", layout="centered")
st.title("About")
left, right = st.columns(2)

with left:
    st.subheader("Repository")
    github_col1, github_col2 = st.columns([0.07, 0.93])
    with github_col1:
        st.image(
            "https://www.iconninja.com/files/328/954/550/github-icon.png", width=24
        )
    with github_col2:
        st.markdown(
            "[AB Calculator on GitHub](https://github.com/digreen17/ab_calculator)"
        )

with right:
    st.subheader("Contact")
    linkedin_col1, linkedin_col2 = st.columns([0.07, 0.93])
    with linkedin_col1:
        st.image(
            "https://www.iconninja.com/files/272/300/55/linkedin-blue-linkedin-linkedin-logo-icon.png",
            width=24,
        )
    with linkedin_col2:
        st.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")

    telegram_col1, telegram_col2 = st.columns([0.07, 0.93])
    with telegram_col1:
        st.image(
            "https://www.iconninja.com/files/60/1019/664/telegram-icon.png", width=24
        )
    with telegram_col2:
        st.markdown("[Telegram](https://t.me/digreen_17)")

st.divider()
st.subheader("Sample‑Size Calculator")
st.write(
    "Determines the minimum number of observations required per experimental group."
)

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

st.info(
    "After entering the parameters, the calculator outputs the minimum sample size per group."
)
