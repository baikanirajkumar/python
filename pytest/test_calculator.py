from calculator import add
def test_add_positive():
    assert add(10,20)==30


def test_add_negative():
    assert add(-10,-20)==-30

def test_add_zero():
    assert add(10,0)==10
#Pytest : Checks whether code works correctly
# Pytest will find files starting with test_ and execute the test functions.
# Run:pytest
# assert is used to check whether the actual result is equal to the expected result.