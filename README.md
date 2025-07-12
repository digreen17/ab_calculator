## Sample‑Size Calculator

[Link to the app](https://abcalculator-nmf525vjrygaf9rpyabs39.streamlit.app/about)

---

The **Sample‑Size Calculator** determines the minimum number of observations required per experimental group for A/B testing.

### Core Parameters

| Parameter   | Purpose                                |
| ----------- | -------------------------------------- |
| Metric type | Continuous or binary metric            |
| MDE (%)     | Minimum detectable effect              |
| Power (1−β) | Probability of detecting a true effect |
| Alpha (α)   | Significance level                     |

### Additional Parameters

#### Continuous Metric

| Parameter          | Purpose                               |
| ------------------ | ------------------------------------- |
| Mean               | Expected average value                |
| Standard deviation | Expected variability                  |
| Data is skewed?    | Apply variance‑stabilizing correction |

#### Binary Metric

| Parameter | Purpose                      |
| --------- | ---------------------------- |
| p         | Baseline success probability |

---

**After entering the parameters, the calculator outputs the minimum sample size required per group.**
