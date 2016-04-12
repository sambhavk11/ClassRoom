from django.template import RequestContext
from django.http import  HttpResponse
from django.shortcuts import  render
from classapp.models import Attendance
from classapp import models



def storeStudent(request):
    request_context = RequestContext(request)
    if request.method=='POST':
        searchparam=request.POST
        studentID=request.POST["studentID"]
        name=request.POST["studentname"]
        address=request.POST["address"]
        gpa=request.POST["gpa"]
        discipleRecord=request.POST["discrecord"]
        feedback=request.POST["feedback"]
        form=request.POST["form"]
        stuclass=request.POST["class"]
        modules = request.POST["modules"]

        newStudent=models.Student(student_id=studentID,name=name,Class=stuclass,modules=modules,address=address,GPA=gpa,discipleRecord=discipleRecord,feedback=feedback,form=form)
        newStudent.save()
        #newModuledata=models.Modules(student=newStudent, modules=modules)
        #newModuledata.save()


    return render(request,'landing.html')


def markAttendance(request):
    #print "inside search student"
    request_context = RequestContext(request)
    if request.method=='POST':
        attendance=request.POST['attendance']
        nameofst=request.POST['stdname']
        comments=request.POST['comments']
        student=models.Student.objects.get(name=nameofst)
        print student
        newAttendance=Attendance(student_id=student, status=attendance,comments=comments)
        newAttendance.save()
        print attendance+nameofst
    #print "inside search student"
    return HttpResponse("Attendance marked  "+attendance+" for  "+nameofst)
