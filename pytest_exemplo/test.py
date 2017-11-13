import index

def test_calc_total():
	total = index.calc_total(2, 3)
	assert total == 5

def test_calc_multiply():
	result = index.calc_multiply(4, 5)
	assert result == 20