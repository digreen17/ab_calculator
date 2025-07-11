import streamlit as st

st.set_page_config(page_title="About")

st.title("About the Application")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Project Links")
    st.markdown("[Project Repository](https://github.com/digreen17/ab_calculator)")

with col2:
    st.subheader("Other Links")
    st.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")
    st.markdown("[Telegram](https://t.me/digreen_17)")

st.markdown("---")


table_md = """
### The application includes:

#### 1. Sample-size calculator
Calculator for the minimum number of observations in each experimental group.

**Input Parameters**

| Field | Description |
|------|--------------|
| **Metric type** | `continuous` continuous metric <br> `binary` binary metric |
| **MDE (%)** | Minimum Detectable Effect in percent |
| **Power (1−β)** | Probability of detecting an effect if it exists |
| **Alpha (α)** | Statistical significance level  |

If the metric type **`continuous`** is selected, additionally specify:

| Field | Description |
|------|--------------|
| **Mean** | expected mean value |
| **Standard deviation**  | standard deviation |

If the distribution is skewed, check the **Data is skewed?** box — the calculation will apply a correction.

If the metric type **`binary`** is selected, additionally specify:

| Field | Description |
|------|--------------|
| **p** | observed success probability for the binary metric |

"""

st.markdown(table_md, unsafe_allow_html=True)


st.markdown(
    """
1. Fill in the parameters above.
2. The **Minimum sample size** value will appear below —
   the minimum number of observations in each group.
"""
)

st.divider()
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Project Repository")
    st.markdown("- [GitHub](https://github.com/digreen17/ab_calculator)")