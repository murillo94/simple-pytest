import index
import pytest

@pytest.mark.parametrize("test_input, expected_output", 
							[
								(5,25),
								(9,81),
								(10,100)
							])

def test_calc_mult_multiply(test_input, expected_output):
	result = index.calc_mult_multiply(test_input)
	assert result == expected_output
