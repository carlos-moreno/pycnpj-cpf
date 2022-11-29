import pytest

from core.core import calculate_first_digit_cnpj, calculate_first_digit_cpf


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
    """Test positive for function calculate_first_digit_cpf."""
    assert calculate_first_digit_cpf(value) == True


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
    """Test positive for function calculate_first_digit_cnpj."""
    assert calculate_first_digit_cnpj(value) == True
