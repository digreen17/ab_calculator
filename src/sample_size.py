from typing import Literal

import numpy as np
from statsmodels.stats.power import tt_ind_solve_power, zt_ind_solve_power


def ttest(
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
