import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.effect_size import eff_size_binary, eff_size_continuous
from src.solver import calc_power, calc_sample_size


def common_inputs():
    col1, col2 = st.columns(2)
    with col1:
        mde_pct = st.number_input("MDE (%)", min_value=1, max_value=99, value=3, step=1)
        mde = mde_pct / 100
    with col2:
        power = st.number_input(
            "Power (1 - β)", min_value=0.01, max_value=0.99, value=0.80, format="%.2f"
        )

    col3, col4 = st.columns(2)
    with col3:
        alpha = st.number_input(
            "Alpha (α)", min_value=0.00001, max_value=0.99, value=0.05, format="%.5f"
        )
    with col4:
        alternative = st.selectbox(
            "Alternative hypothesis", ("two-sided", "larger", "smaller")
        )

    return mde, power, alpha, alternative


def continuous_inputs(mde: float):
    mean = st.number_input("Mean", min_value=0.01)
    std_dev = st.number_input("Standard deviation", min_value=0.01)
    is_skewed = st.checkbox("Data is skewed?", value=False)
    effect_size = eff_size_continuous(mde, mean, std_dev, is_skewed)
    return effect_size, dict(mean=mean, std_dev=std_dev, is_skewed=is_skewed)


def binary_inputs(mde: float):
    p = st.number_input(
        "p - observed success rate",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        format="%.2f",
    )
    effect_size = eff_size_binary(mde, p)
    return effect_size, dict(p=p)


st.set_page_config(page_title="Sample-size calculator", layout="wide")
st.title("Sample‑size calculator")

main_col, chart_col = st.columns([1.3, 1])

with main_col:
    metric_type = st.selectbox("Metric type", ("continuous", "binary"))
    mde, power, alpha, alternative = common_inputs()

    with st.expander(f"{metric_type.capitalize()} metric parameters", expanded=True):
        if metric_type == "continuous":
            effect_size, _ = continuous_inputs(mde)
        else:
            effect_size, _ = binary_inputs(mde)

    sample_size = calc_sample_size(effect_size, alpha, power, alternative)
    total = sample_size * 2

    st.markdown("---")
    col_a, col_b = st.columns(2)
    col_a.metric("Sample size per variant", f"{sample_size:,}")
    col_b.metric("Total sample size (two groups)", f"{total:,}")
# -----------------------------------------------------------------------------


with chart_col:
    st.markdown("### Visualization")
    st.info("📊 тут будет график")
    n_grid = np.linspace(0.01, sample_size * 2, 1000, dtype=int)
    power_curve = np.array(
        [calc_power(effect_size, n, alpha, alternative) for n in n_grid]
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=power_curve,
            name="Power",
            mode="lines",
            line=dict(width=3, color="royalblue"),
        )
    )

    fig.update_layout(
        xaxis_title="Sample size",
        legend=dict(orientation="h", y=1.05, x=0.5, xanchor="center"),
    )

    fig.update_xaxes(showspikes=True, spikecolor="green",
                 spikethickness=2, spikedash="dash")   # вертикаль
    fig.update_yaxes(showspikes=True, spikecolor="green",
                 spikethickness=2, spikedash="dash")   # горизонталь
    # fig.update_layout(hovermode="x unified")               # единая подсветка по X


    st.plotly_chart(fig, use_container_width=True)
