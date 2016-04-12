from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render
from classapp.models import Teacher


def errorpage(request):
    return render(request, 'errorpage.html')


def usersignup(request):
    if request.method == 'POST':

        request_context = RequestContext(request)
        username = request.POST['username']
        password = request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(email, email, password)
        newTeacher=Teacher(name=username,email=email,address=email)
        newTeacher.save()
        return render(request,'login.html')


