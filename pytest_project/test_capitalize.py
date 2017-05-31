import pytest
from .main import capital_case


def test_capitalize_case():
    assert capital_case('semper fidelis') == 'Semper fidelis'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
