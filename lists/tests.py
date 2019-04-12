from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Courses


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_correct(self):
            
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_save_POST_request(self):
        response = self.client.post('/', data = {'course_text': 'A new Course'})

        self.assertEqual(Courses.objects.count(), 1)
        new_course = Courses.objects.first()
        self.assertEqual(new_course.text, 'A new Course')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_save_courses_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Courses.objects.count(), 0)

    def test_redirecct_after_POST(self):
        response = self.client.post('/', data={'course_text': 'A new Course'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_display_all_courses(self):
        Courses.objects.create(text = 'Course1')
        Courses.objects.create(text = 'Course2')

        response = self.client.get('/')

        self.assertIn('Course1',  response.content.decode())
        self.assertIn('Course2',  response.content.decode())


class CourseModelTest(TestCase):
    def test_save_and_retrieve_courses(self):
        first_course = Courses()
        first_course.text = 'First Course'
        first_course.save()

        second_course = Courses()
        second_course.text = 'Second Course'
        second_course.save()

        saved_Courses = Courses.objects.all()
        self.assertEqual(saved_Courses.count(), 2)

        first_saved_course = saved_Courses[0]
        second_saved_course = saved_Courses[1]
        self.assertEqual(first_saved_course.text, 'First Course')
        self.assertEqual(second_saved_course.text, 'Second Course')