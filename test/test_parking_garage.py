from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from mock import GPIO


class TestParkingGarage(TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        pass

