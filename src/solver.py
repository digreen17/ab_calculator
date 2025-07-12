import numpy as np
from statsmodels.stats.power import tt_ind_solve_power


def calc_sample_size(
    effect_size: float,
    alpha: float,
    power: float,
) -> int:

    sample_size = tt_ind_solve_power(
        effect_size=effect_size,
        nobs1=None,
        alpha=alpha,
        power=power,
        ratio=1,
    )
    return int(np.ceil(sample_size))


def calc_power(
    effect_size: float,
    nobs1: int,
    alpha: float,
) -> float | None:
    power = tt_ind_solve_power(
        effect_size=effect_size,
        nobs1=nobs1,
        alpha=alpha,
        power=None,
        alternative="two-sided",
        ratio=1,
    )
    return float(power)


def calc_effect_size(
    nobs1: int,
    alpha: float,
    power: float,
) -> float | None:
    effect_size = tt_ind_solve_power(
        effect_size=None,
        nobs1=nobs1,
        alpha=alpha,
        power=power,
        ratio=1,
    )
    return float(abs(effect_size))
