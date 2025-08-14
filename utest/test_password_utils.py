import pytest

from password_utils import is_strong_password


# def test_length_of_password():
#     assert is_strong_password("Secure12345") == True, "Password must have length >= 8"
    
# def test_password_have_capital():
#     assert is_strong_password("password2345") is True, "Must include at lest one capital letter"
    
    
# def test_password_have_small():
#     assert is_strong_password("SMALLe334"), "Must include at lest one small letter"
    
# def test_password_have_digit():
#     assert is_strong_password("Digitsuihnisfdj") is False, "Must include at lest one digit"
    


@pytest.mark.parametrize("password, expected, message",[
    ("Secur", True, "Test for length is failed!"),
    ("password2345", False, "the test for Capital failed"),
    ("SMALL334", False, "function is not working for detecting small letters"),
    ("Digits212", True, "Must include at lest one digit")
])
def test_validate_password(password, expected, message):
    assert is_strong_password(password) == expected, message
