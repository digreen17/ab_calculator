import streamlit as st
from src.sample_size import ttest, ztest
from src.effect_size import eff_size_continuous, eff_size_binary



st.title("Sample size calculator")

metric_type = st.selectbox("Select metric type:",
                     ("continuous", "binary"))
st.write("You choose:", metric_type)

if metric_type == "continuous":
    is_skewed = st.checkbox("Data is skewed")
    st.write(is_skewed)
    mde = st.slider("MDE",
                min_value=0.01,
                max_value=0.99,
                value=0.03,
                step=0.01)
    power = st.number_input("Power",
                min_value=0.00,
                max_value=0.99,
                value=0.80,
                format="%.2f")

    alpha = st.number_input("alpha",
                min_value=0.0,
                max_value=0.99,
                value=0.05, 
                format="%.5f")
    
    alternative = st.selectbox("Select alternative hypothesis:",
                           ("two-sided", "larger", "smaller"))
    
    mean = st.number_input("mean",
                           min_value=0.01,
                           )
    
    std_dev = st.number_input("std_dev",
                           min_value=0.01,
                           )
    
    effect_size = eff_size_continuous(mde, mean, std_dev, is_skewed)
    
    st.write("Sample size", ttest(effect_size, alpha, power, alternative))

elif metric_type == "binary":
    mde = st.slider("MDE",
                min_value=0.01,
                max_value=0.99,
                value=0.03,
                step=0.01)
    power = st.number_input("Power",
                min_value=0.00,
                max_value=0.99,
                value=0.80,
                format="%.2f")

    alpha = st.number_input("alpha",
                min_value=0.0,
                max_value=0.99,
                value=0.05, 
                format="%.5f")
    
    alternative = st.selectbox("Select alternative hypothesis:",
                           ("two-sided", "larger", "smaller"))
    
    p = st.number_input("p - observed success rate",
                        min_value=0.00,
                        max_value=1.00,
                        value=0.50,
                        format="%.2f")
    effect_size = eff_size_binary(mde, p)
    st.write("Sample size", ztest(effect_size, alpha, power, alternative))
    













