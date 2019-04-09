from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):
    def test_url_resolves_home_page(self):
        found = resolve('/') 
        self.assertEqual(found.func, home_page)  
asdasdasd

    def test_home_page_correct(self):
            request = HttpRequest()  
            response = home_page(request)  
            html = response.content.decode('utf8')  
            self.assertTrue(html.startswith('<html>'))  
            self.assertIn('<title>Course Management</title>', html)  
            self.assertTrue(html.endswith('</html>')) 
