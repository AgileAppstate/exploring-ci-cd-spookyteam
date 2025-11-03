
from helloworld import greet  # see note below

def test_greet_default():
    assert greet() == "Hello, world!"
def test_greet_custom():
     assert greet("AppState") == "Hello, AppState!"

