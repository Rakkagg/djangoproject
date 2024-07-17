# tests.py
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Test if the root URL resolves to the home_page view."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Test if the home_page view returns the correct HTML."""
        request = HttpRequest()
        response = home_page(request)

        # Ensure the response content starts with <html> and ends with </html>
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
