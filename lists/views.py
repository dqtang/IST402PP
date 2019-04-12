from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Courses


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Courses.objects.create(text=request.POST['course_text'])
        return redirect('/')

    courses = Courses.objects.all()
    return render(request, 'home.html', {'courses' : courses})