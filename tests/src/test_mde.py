import re

import numpy as np
import pytest

from src.mde import mde_binary, mde_continuous


class TestMdeContinuous:
    @pytest.mark.parametrize(
        "eff_size, mean, std_dev, is_skewed, expected",
        [
            (3.0, 2.0, 4.0, False, 3.0 * 4.0 / 2.0),
            (3.0, 2.0, 4.0, True, 3.0 * np.log1p(4.0) / np.log1p(2.0)),
        ],
    )
    def test_happy_cont_mde(self, eff_size, mean, std_dev, is_skewed, expected):
        mde = mde_continuous(eff_size, mean, std_dev, is_skewed)
        assert mde == expected

    @pytest.mark.parametrize(
        "eff_size, mean, std_dev",
        [
            (-3.0, 2.0, 4.0),
            (3.0, -2.0, 4.0),
            (3.0, 2.0, -4.0),
            (0, 2.0, 4.0),
            (3.0, 0, 4.0),
            (3.0, 2.0, 0),
        ],
    )
    def test_invalid_cont_mde(self, eff_size, mean, std_dev):
        with pytest.raises(ValueError, match="All arguments should be positive"):
            mde_continuous(eff_size, mean, std_dev, is_skewed=False)


class TestMdeBinary:
    @pytest.mark.parametrize(
        "eff_size, p, expected", [(2.0, 0.5, 2.0 * np.sqrt(0.5 * (1 - 0.5)))]
    )
    def test_happy_bin_mde(self, eff_size, p, expected):
        mde = mde_binary(eff_size, p)
        assert mde == expected

    def test_invalid_effsize(self):
        with pytest.raises(ValueError, match="`eff_size` should be positive"):
            mde_binary(-1.0, 0.5)

    @pytest.mark.parametrize(
        "eff_size, p",
        [
            (1.0, -0.1),
            (1.0, 1.1),
        ],
    )
    def test_invalid_p(self, eff_size, p):
        with pytest.raises(
            ValueError, match=re.escape("`p` should be in range (0 ... 1)")
        ):
            mde_binary(eff_size, p)
