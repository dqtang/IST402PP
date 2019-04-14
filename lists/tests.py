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


class NewListTest(TestCase):
    def test_save_POST_request(self):
        self.client.post('/lists/new', data = {'course_text': 'A new Course'})
        self.assertEqual(Courses.objects.count(), 1)
        new_course = Courses.objects.first()
        self.assertEqual(new_course.text, 'A new Course')

  

    def test_redirecct_after_POST(self):
        response = self.client.post('/lists/new', data={'course_text': 'A new Course'})
        self.assertRedirects(response, '/lists/best-course-list/')


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


class ListViewTest(TestCase):
    
    def test_use_list_template(self):
        response = self.client.get('/lists/best-course-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_courses(self):
        Courses.objects.create(text = 'Course1')
        Courses.objects.create(text = 'Course2')

        response = self.client.get('/lists/best-course-list/')

        self.assertContains(response, 'Course1')
        self.assertContains(response, 'Course2')
