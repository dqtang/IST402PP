from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Courses, List


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list' : list_})

def new_list(request):
    list_ = List.objects.create()
    Courses.objects.create(text=request.POST['course_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_course(request, list_id):
    list_ = List.objects.get(id=list_id)
    Courses.objects.create(text = request.POST['course_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')