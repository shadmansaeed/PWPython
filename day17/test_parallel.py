'''
Pre-requisite:  Install a pytest plugin "pytest-xdist" to run tests parallel
pip install pytest-xdist
'''


def test_one():
    print("running test one")
    assert True


def test_two():
    print("running test two")
    assert True


def test_three():
    print("running test three")
    assert True


def test_four():
    print("running test four")
    assert True


"""
to run the test parallely:

pytest day17/test_parallel.py -v -s -n 2

"""