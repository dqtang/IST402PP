from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Courses


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    courses = Courses.objects.all()
    return render(request, 'list.html', {'courses' : courses})

def new_list(request):
    Courses.objects.create(text=request.POST['course_text'])
    return redirect('/lists/best-course-list/')
