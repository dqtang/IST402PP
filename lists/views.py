from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Courses, List


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    courses = Courses.objects.all()
    return render(request, 'list.html', {'courses' : courses})

def new_list(request):
    list_ = List.objects.create()
    Courses.objects.create(text=request.POST['course_text'], list=list_)
    return redirect('/lists/best-course-list/')
