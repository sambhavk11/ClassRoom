from django.template import RequestContext
from classapp.models import Student

from django.http import HttpResponse
from django.shortcuts import render



def searchVal(request):
    #print "inside search student"
    request_context = RequestContext(request)
    if request.method=='POST':
        searchparam=request.POST['searchField']
        print searchparam
        stdData=Student.objects.filter(name=searchparam).values()
        print stdData
    #print "inside search student"
    return render(request,'searchresults.html',{'student':stdData})


def loadStuDetails(request):
    request_context = RequestContext(request)
    if request.method == 'GET':
        nameofst = request.GET['stdname']
        print "hey there inside load "+nameofst
        stdData = Student.objects.filter(name=nameofst).values()
    return render(request,'studentdetails.html',{'student':stdData})

