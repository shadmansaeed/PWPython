'''
grouping tests:
--------------
test_LoginByEmail -> sanity , regression
test_LoginByFacebook -> sanity
test_LoginByPhone -> regression
test_signupByEmail -> sanity, regression
test_signupByFacebook -> regression
test_signupbyphone -> sanity
test_paymentindollor -> sanity, regression
test_paymentinrupees -> regression

'''

import pytest


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.skip
def test_LoginByEmail():
    print("This is login by email test")
    assert True == True


@pytest.mark.sanity
def test_LoginByFacebook():
    print("This is login by facebook test")
    assert 1 == 1


@pytest.mark.regression
def test_LoginByPhone():
    print("This is login by phone test")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyEmail():
    print("This is signup by email test")
    assert 1 == 1


@pytest.mark.regression
def test_signupbyFacebook():
    print("This is signup by facebook test")
    assert True == True


@pytest.mark.sanity
def test_signupbyPhone():
    print("This is signup by phone test")
    assert True == True


@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollor():
    print("This is signup by phone test")
    assert 1 == 1


@pytest.mark.regression
def test_paymentinrupees():
    print("This is signup by phone test")
    assert 1 == 1


'''
1. run sanity test--> pytest day17/test_grouping.py -v -s -m "sanity"
2. run only regression--> pytest day17/test_grouping.py -v -s -m "regression"

3. run test which are belong to both sanity and regression--> pytest day17/test_grouping.py -v -s -m "sanity and regression"

4. run only sanity tests which are not belongs to regression--> pytest day17/test_grouping.py -v -s -m "sanity" -m "not regression"

5. run only regression tests which are not belongs to sanity--> pytest day17/test_grouping.py -v -s -m "regression" -m "not sanity"
 
'''