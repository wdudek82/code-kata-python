import os
import sys
sys.path.append("../copy_biggest.py")

import pytest

from ..copy_biggest import copy_biggest_files


mock_source = os.path.abspath("mock_source")
mock_destination = os.path.abspath("mock_destination")


def test_rasies_the_exception_if_number_arg_is_a_float():
    with pytest.raises(TypeError):
        copy_biggest_files(mock_source, mock_destination, 0.5)

def test_raises_the_exception_if_number_arg_is_a_string():
    with pytest.raises(TypeError):
        copy_biggest_files(mock_source, mock_destination, 'a')

def test_raises_the_exception_if_source_is_not_a_string():
    with pytest.raises(NotADirectoryError):
        copy_biggest_files(6, mock_destination, 0)
