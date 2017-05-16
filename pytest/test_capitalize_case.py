import sys
sys.path.append("main_script.py")

import pytest

from main_script import capital_case


def test_capital_case():
    assert capital_case("blabla bla") == "Blabla bla"

def test_raises_the_exception_on_non_string_argument():
    with pytest.raises(TypeError):
        capital_case(9)
