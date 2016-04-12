from django.template import RequestContext
from classapp.models import Student

from django.http import HttpResponse
from django.shortcuts import render
from classapp.models import Attendance



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


def markAttendance(request):
    #print "inside search student"
    request_context = RequestContext(request)
    if request.method=='POST':
        attendance=request.POST['attendance']
        nameofst=request.POST['stdname']
        student=Student.objects.get(name=nameofst)
        print student
        newAttendance=Attendance(student_id=student, status=attendance)
        newAttendance.save()
        print attendance+nameofst
    #print "inside search student"
    return HttpResponse(attendance+"  "+nameofst)

def loadStuDetails(request):
    request_context = RequestContext(request)
    if request.method == 'GET':
        nameofst = request.GET['stdname']
        print "hey there inside load "+nameofst
        stdData = Student.objects.filter(name=nameofst).values()
    return render(request,'studentdetails.html',{'student':stdData})

