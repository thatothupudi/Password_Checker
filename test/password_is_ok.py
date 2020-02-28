from password_checker.password_check import Password

# Testing password is valid
password_ok = Password()

def test_password_is_ok():
    assert password_ok.password_is_ok("That1thup@d!") == True
    