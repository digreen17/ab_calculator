import re

import numpy as np
import pytest

from src.effect_size import eff_size_binary, eff_size_continuous


class TestContinuous:
    @pytest.mark.parametrize(
        "mde, mean, std_dev, is_skewed, expected",
        [
            (5.0, 6.0, 2.0, False, (5.0 * 6.0 / 2.0)),
            (5.0, 6.0, 2.0, True, (5.0 * np.log1p(6.0) / np.log1p(2.0))),
        ],
    )
    def test_happy_continuous(self, mde, mean, std_dev, is_skewed, expected):
        eff_size_result = eff_size_continuous(mde, mean, std_dev, is_skewed)
        assert eff_size_result == expected

    @pytest.mark.parametrize(
        "mde, mean, std_dev",
        [
            (-5.0, 6.0, 2.0),
            (5.0, -6.0, 2.0),
            (5.0, 6.0, -2.0),
        ],
    )
    def test_invalid_continuous(self, mde, mean, std_dev):
        with pytest.raises(ValueError, match="All arguments should be positive"):
            eff_size_continuous(mde, mean, std_dev, is_skewed=False)


class TestBinary:
    @pytest.mark.parametrize(
        "mde, p, expected",
        [
            (5.0, 0.5, 5 / np.sqrt(0.5 * (1 - 0.5))),
            (2.0, 0.25, 2.0 / np.sqrt(0.25 * (1 - 0.25))),
        ],
    )
    def test_happy_binary(self, mde, p, expected):
        eff_size_result = eff_size_binary(mde, p)
        assert eff_size_result == expected

    def test_invalid_mde_binary(self):
        with pytest.raises(ValueError, match="`mde` should be positive"):
            eff_size_binary(0, 0.5)

    @pytest.mark.parametrize("mde, p", [(5.0, -1.5), (5.0, 1.5)])
    def test_invalid_p_binary(self, mde, p):
        with pytest.raises(
            ValueError, match=re.escape("`p` should be in range (0 ... 1)")
        ):
            eff_size_binary(mde, p)
