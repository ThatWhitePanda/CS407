from divisors import divisors

def test_one():
	assert divisors(1) == [1]

def test_2():
	assert divisors(2) == [1, 2]

def test_26():
	assert divisors(26) == [1, 2, 13, 26]
