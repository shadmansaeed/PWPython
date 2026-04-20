# Fixture : Re-usable function

import pytest 


# functional approach

@pytest.fixture
def setup():
    print("setup browser..")
    yield
    print("close browser")


def test_one(setup):
    print("This is my test one")


def test_two(setup):
    print("This is my test two")


def test_three(setup):
    print("This is my test three")


# method approach
# class TestClass():
#     def test_one(self):  # self is mandatory when under class
#         print("This is my test one") # under class, these are called methods
#
#     def test_two(self):
#         print("This is my test two")
#
#     def test_three(self):
#         print("This is my test three")


'''
To run all the tests in the module
    pytest test_demos.py
    pytest test_demos.py -s
    pytest test_demos.py -s -v

To run specific test in the module
    pytest test_demos.py::test_one -s -v
    pytest test_demos.py::test_two -s -v
    pytest test_demos.py::test_three -s -v

-s  : you can see all print() outputs live in the console while the test runs.
-v :  Runs pytest in verbose mode. Shows detailed test execution information.

'''
