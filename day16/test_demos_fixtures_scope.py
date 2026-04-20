# Fixture : Re-usable function

# scope="function"  fixture will be called before every test function executes
# scope="module"   fixture will be called only once before test functions executes
# scope="class"   fixture will be called only once before the class
# scope="session"  fixture will be called only once for session


# module --> class --> methods
# module --> function

import pytest


@pytest.fixture
def setup(scope="module"):
    print("setup browser..")

def test_one(setup):
    print("This is my test one")


def test_two(setup):
    print("This is my test two")


def test_three(setup):
    print("This is my test three")


# '''
# To run all the tests in the module
#     pytest test_demos.py
#     pytest test_demos.py -s
#     pytest test_demos.py -s -v
#
# To run specific test in the module
#     pytest test_demos.py::test_one -s -v
#     pytest test_demos.py::test_two -s -v
#     pytest test_demos.py::test_three -s -v
#
# -s  : you can see all print() outputs live in the console while the test runs.
# -v :  Runs pytest in verbose mode. Shows detailed test execution information.
#
# '''
