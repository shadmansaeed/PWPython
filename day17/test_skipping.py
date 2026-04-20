import pytest


def test_LoginByEmail():
    print("This is login by email test")
    assert True == True


@pytest.mark.skip
def test_LoginByFacebook():
    print("This is login by facebook test")
    assert 1 == 1


@pytest.mark.skip
def test_LoginByPhone():
    print("This is login by phone test")
    assert 1 == 1


def test_signupbyEmail():
    print("This is signup by email test")
    assert 1 == 1


@pytest.mark.skip
def test_signupbyFacebook():
    print("This is signup by facebook test")
    assert True == True


@pytest.mark.skip
def test_signupbyPhone():
    print("This is signup by phone test")
    assert True == True
