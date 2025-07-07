from typing import Literal

import numpy as np
from statsmodels.stats.power import tt_ind_solve_power


def calc_sample_size(
    effect_size: float,
    alpha: float,
    power: float,
    alternative: Literal["two-sided", "larger", "smaller"],
) -> int:
    sample_size = tt_ind_solve_power(
        effect_size=effect_size,
        nobs1=None,
        alpha=alpha,
        power=power,
        alternative=alternative,
        ratio=1,
    )
    return int(np.ceil(sample_size))


def calc_power(
    effect_size: float,
    nobs1: int,
    alpha: float,
    alternative: Literal["two-sided", "larger", "smaller"],
) -> float:
    power = tt_ind_solve_power(
        effect_size=effect_size,
        nobs1=nobs1,
        alpha=alpha,
        power=None,
        alternative=alternative,
    )
    return power


def calc_effect_size(
    nobs1: int,
    alpha: float,
    power: float,
    alternative: Literal["two-sided", "larger", "smaller"],
) -> float:
    effect_size = tt_ind_solve_power(
        effect_size=None, nobs1=nobs1, alpha=alpha, power=power, alternative=alternative
    )
    return abs(effect_size)


calc_effect_size(20, 0.5, 0.8, "two-sided")
# def calc_mde(
#     nobs1: int,
#     alpha: float,
#     power: float,
#     alternative: Literal["two-sided", "larger", "smaller"],

#     ) ->
