from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestOverflow(TestCase):
    """
    This class contains tests that calculate the amount of water poured in specific location
    """
    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client()
        self.url = reverse("wateroverflow:overflow")

    def test_calculation(self):
        """
        Test the calculation
        """
        data = {
            "row" : 10,
            "glass": 3,
            "water": 15
        }

        response = self.client.post(self.url, data)

        self.assertContains(response, '0.14453125L')