from django.template import RequestContext
from django.http import  HttpResponse
from django.shortcuts import  render

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