import pytest

from core.core import (
    first_digit_cnpj_checker_is_valid,
    first_digit_cpf_checker_is_valid,
)


@pytest.mark.unit
@pytest.mark.high
@pytest.mark.parametrize(
    "value",
    [
        "98803280278",
        "71858204054",
        "06982641007",
        "89219560003",
        "53683761032",
    ],
)
def test_positive_first_digit_cpf(value):
    """Test positive for function first_digit_cpf_checker_is_valid."""
    assert first_digit_cpf_checker_is_valid(value) == True


@pytest.mark.unit
@pytest.mark.high
@pytest.mark.parametrize(
    "value",
    [
        "97744421000169",
        "89420356000198",
        "50629870000100",
        "88506571000143",
        "35868665000104",
    ],
)
def test_positive_first_digit_cnpj(value):
    """Test positive for function first_digit_cnpj_checker_is_valid."""
    assert first_digit_cnpj_checker_is_valid(value) == True
