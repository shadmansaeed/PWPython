# -------------------------------------------------------------------
# Test: Create Booking (POST request with static body)
# Request Type: POST
# Data : Hardcoded data inside the test
# -------------------------------------------------------------------
from urllib import response

from playwright.sync_api import Playwright, expect


def test_create_booking(playwright: Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()

    request_body = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 5000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response= request_context.post(f"{base_url}/booking", data=request_body)

    # validation
    #expect(response_body).to_be_ok()

    assert response.ok
    assert response.status==200
    response_body= response.json()
    print("Response body=======>",response_body)

    assert "bookingid"
