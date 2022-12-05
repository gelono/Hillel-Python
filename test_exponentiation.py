import pytest
from Hillel.library import non_negative_exponentiation_of_args_product  # type: ignore


@pytest.mark.parametrize('arg_1, arg_2, exponent, expected', [(2, 3, 4, int), (2.1, 3.5, 4.5, float)])
def test_type_of_exponentiation_of_args_product(arg_1, arg_2, exponent, expected):
    return_type = non_negative_exponentiation_of_args_product(arg_1, arg_2, exponent=exponent)
    assert type(return_type) == expected, 'Unexpected type return'


@pytest.mark.parametrize('arg_1, arg_2, exponent, expected', [(1, 2, 2, 4), (1, 3, 2., 9.), (-2, 3, 2, 36)])
def test_value_of_exponentiation_of_args_product(arg_1, arg_2, exponent, expected):
    return_value = non_negative_exponentiation_of_args_product(arg_1, arg_2, exponent=exponent)
    assert return_value == expected, 'Unexpected value'


@pytest.mark.parametrize('arg_1, arg_2, exponent, error', [(1, '2', 2, TypeError), (1, 2, -2, ValueError)])
def test_errors_exponentiation_of_args_product(arg_1, arg_2, exponent, error):
    with pytest.raises(error):
        non_negative_exponentiation_of_args_product(arg_1, arg_2, exponent=exponent)
