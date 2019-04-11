from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_correct(self):
            
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_save_POST_request(self):
        response = self.client.post('/', data = {'course_text': 'A new Course'})
        self.assertIn('A new Course', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')