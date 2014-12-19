from django.test import TestCase
from django.test import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class SmokeTest(TestCase):

    def test_home_page_loads(self):
        """Tests that the home page loads."""
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 302)
