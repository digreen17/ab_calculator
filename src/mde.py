import numpy as np


def mde_continuous(
    eff_size: float, mean: float, std_dev: float, is_skewed: bool
) -> float:
    if any(arg <= 0 for arg in (eff_size, mean, std_dev)):
        raise ValueError(
            f"All arguments should be positive: {eff_size}, {mean}, {std_dev}"
        )
    if is_skewed:
        mean = np.log1p(mean)
        std_dev = np.log1p(std_dev)
    mde = eff_size * std_dev / mean
    return mde


def mde_binary(eff_size: float, p: float) -> float:
    if eff_size <= 0:
        raise ValueError("`mde` should be positive")
    if p < 0 or p > 1:
        raise ValueError("`p` should be in range (0 ... 1)")
    sigma_binary = np.sqrt(p * (1 - p))
    mde = eff_size * sigma_binary
    return mde
