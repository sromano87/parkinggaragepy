from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock

class TestParkingGarage(TestCase):

    @patch.object(SomeClassOrModule, 'someCallable')
    def test_something(self, mock_method: Mock):
        # Your test

