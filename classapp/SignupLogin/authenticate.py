from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render

def authenticateUser(request):

    if request.method == 'POST':
       request_context = RequestContext(request)
       email = request.POST.get('email',False)
       logpassword = request.POST.get('password',False)
       user = authenticate(username=email,password=logpassword)

    if user is not None:
    # the password verified for the user
       if user.is_active:
           login(request,user)
           return render(request,'landing.html')
       else:
           return HttpResponse("User Inactive")
    else:
    # the authentication system was unable to verify the username and password
        return HttpResponse("User Cannot be Authenticated. Check Username or password")