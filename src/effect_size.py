import numpy as np


def eff_size_continuous(
    mde: float, mean: float, std_dev: float, is_skewed: bool
) -> float:
    if any(arg <= 0 for arg in (mde, mean, std_dev)):
        raise ValueError("All arguments should be positive")
    if is_skewed:
        mean = np.log1p(mean)
        std_dev = np.log1p(std_dev)
    eff_size = mde * mean / std_dev
    return eff_size


def eff_size_binary(mde: float, p: float) -> float:
    if mde <= 0:
        raise ValueError("`mde` should be positive")
    if p < 0 or p > 1:
        raise ValueError("`p` should be in range (0 ... 1)")
    sigma_binary = np.sqrt(p * (1 - p))
    eff_size = mde / sigma_binary
    return eff_size
