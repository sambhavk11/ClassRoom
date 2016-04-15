"""ClassRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import classapp.views
from classapp.SignupLogin import signup,authenticate
from classapp.DataAccess import storeData
from classapp.DataAccess import searchStudent
from ClassRoom import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', classapp.views.loadlogin),
    url(r'^login', classapp.views.loadlogin),
    url(r'^loadsearch', classapp.views.loadsSearchResults),
    url(r'^signup', classapp.views.loadSignup),
    url(r'^studentDetails',searchStudent.loadStuDetails),
    url(r'^teacher', classapp.views.loadTeachDetails),
    url(r'^callSignup', signup.usersignup),
    url(r'^callAuthenticate',authenticate.authenticateUser),
    url(r'^storeStudent', storeData.storeStudent),
    url(r'^searchStudent', searchStudent.searchVal),
    url(r'^markAttendance',storeData.markAttendance),
    url(r'^uploadPicpage', storeData.loaduploadPic),
    url(r'^callupload', storeData.callUpload),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,}),

]
