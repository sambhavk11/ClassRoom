from django.shortcuts import render

# Create your views here.

def loadHomePage(request):
    return render(request,'landing.html')
def loadlogin(request):
    return render(request,'login.html')
def loadsSearchResults(request):
    return render(request,'searchresults.html')
def loadSignup(request):
    return render(request,'signup.html')
def loadStuDetails(request):
    return render(request,'studentdetails.html')
def loadTeachDetails(request):
    return render(request,'teacherdetails.html')

