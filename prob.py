from collections.abc import Iterable

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from src.effect_size import eff_size_binary, eff_size_continuous
from src.mde import mde_binary, mde_continuous
from src.solver import calc_effect_size, calc_power, calc_sample_size

N_GRID_MIN: int = 10
N_GRID_POINTS: int = 1000


def common_inputs() -> tuple:
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
            "Alpha (α)", min_value=0.00001, max_value=0.99, value=0.05, format="%g"
        )
    with col4:
        alternative = st.selectbox(
            "Alternative hypothesis", ("two-sided", "larger", "smaller")
        )

    return mde, power, alpha, alternative


def continuous_inputs() -> tuple:
    mean = st.number_input("Mean", min_value=0.01)
    std_dev = st.number_input("Standard deviation", min_value=0.01)
    is_skewed = st.checkbox("Data is skewed?", value=False)
    return mean, std_dev, is_skewed


def binary_inputs() -> tuple:
    p = st.number_input(
        "p - observed success rate",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        format="%.2f",
    )
    return (p,)


METRIC_HANDLERS = {
    "continuous": {
        "inputs": continuous_inputs,
        "effect_size": eff_size_continuous,
        "mde": mde_continuous,
    },
    "binary": {
        "inputs": binary_inputs,
        "effect_size": eff_size_binary,
        "mde": mde_binary,
    },
}

st.set_page_config(page_title="Sample-size calculator", layout="wide")
st.title("Sample‑size calculator")


def create_power_mde_plot(
    n_grid: Iterable[int],
    power_curve: Iterable[float],
    mde_curve: Iterable[float],
    sample_size: int,
) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=power_curve,
            name="Power",
            line_color="royalblue",
            line_width=3,
            customdata=mde_curve,
            hovertemplate=(
                "Sample size: %{x:,.0f}<br>"
                "Power: %{y:.3f}<br>"
                "MDE: %{customdata:.3f} %<extra></extra>"
            ),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=n_grid,
            y=mde_curve,
            name="MDE (%)",
            line_width=3,
            line_color="magenta",
            yaxis="y2",
            hovertemplate=(
                "Sample size: %{x:,.0f}<br>" "MDE: %{y:.3f} %<extra></extra>"
            ),
        )
    )

    fig.add_shape(
        type="line",
        x0=sample_size,
        x1=sample_size,
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line_color="green",
        line_width=3,
        line_dash="dot",
        layer="above",
    )

    fig.update_layout(
        xaxis_title="Sample size",
        yaxis=dict(title="Power", range=[0, 1]),
        yaxis2=dict(title="MDE (%)", overlaying="y", side="right", range=[0, 100]),
        legend=dict(orientation="h", x=0.9, y=-0.2, xanchor="center", yanchor="top"),
    )
    fig.update_xaxes(
        showspikes=True, spikecolor="green", spikethickness=2, spikedash="dash"
    )

    fig.update_yaxes(
        showspikes=True, spikecolor="green", spikethickness=2, spikedash="dash"
    )

    return fig


main_col, chart_col = st.columns([1.5, 1])

with main_col:
    metric_type = st.selectbox("Metric type", ("continuous", "binary"))
    mde, power, alpha, alternative = common_inputs()

    with st.expander(f"{metric_type.capitalize()} metric parameters", expanded=True):
        handler = METRIC_HANDLERS[metric_type]
        param = handler["inputs"]()
        effect_size = handler["effect_size"](mde, *param)

    sample_size = calc_sample_size(effect_size, alpha, power, alternative)

    st.markdown(f"## Sample size:&nbsp;&nbsp;:red[**{sample_size:,}**]")


with chart_col:
    st.markdown("## Visualization")
    n_grid = np.linspace(N_GRID_MIN, sample_size * 2, N_GRID_POINTS, dtype=int)
    power_curve = [calc_power(effect_size, n, alpha, alternative) for n in n_grid]
    eff_size_curve = [calc_effect_size(n, alpha, power, alternative) for n in n_grid]
    mde_curve = [handler["mde"](e, *param) * 100 for e in eff_size_curve]
    fig = create_power_mde_plot(n_grid, power_curve, mde_curve, sample_size)
    st.plotly_chart(fig, use_container_width=True)
