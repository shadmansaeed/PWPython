'''
pre-requisite : install pytest-order plugin

    # pip install pytest-ordering    # deprecated

     pip install pytest-order
'''

import pytest


# Approach 1: order test by position

# @pytest.mark.order(3)
# def test_logout():
#     print("This is logout")
#
#
# @pytest.mark.order(2)
# def test_add_item():
#     print("This is add item test")
#
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")


# Approach 2: Using before, after

# @pytest.mark.order(after="test_add_item")
# def test_checkout():
#     print("This is checkout")
#
#
# @pytest.mark.order(before="test_checkout")
# def test_add_item():
#     print("This is add item test")
#
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is login test")


# Approach 3: using marker string ( user defined)

@pytest.mark.order("last")
def test_checkout():
    print("This is checkout")


@pytest.mark.order("first")
def test_login():
    print("This is login test")

@pytest.mark.order()
def test_add_item():
    print("This is add item test")






