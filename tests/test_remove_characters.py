import pytest

from pycpf_cnpj.core import extract_digits


@pytest.mark.unit
@pytest.mark.high
@pytest.mark.parametrize(
    "value",
    [
        "111.111.111-11",
        "222.222.222-22",
        "123.456.789-10",
        "844.205.110-44",
        "104.256.830-87",
        "50.822.716/0001-42",
        "73.295.178/0001-80",
        "86.287.647/0001-61",
        "11.222.345/0001-43",
    ],
)
def test_positive_extract_digits(value):
    """Test positive for function remove_characters."""
    assert extract_digits(value).isdigit() == True
