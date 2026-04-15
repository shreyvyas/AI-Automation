import pytest

def test_loginUser(setup_testdata):
    print(setup_testdata["username"])
    print(setup_testdata["password"])



def test_openBrowser(setup):
    print("Browser is opened and running")