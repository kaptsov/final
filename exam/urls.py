"""final URL Configuration

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
from django.conf.urls import url, include
from . import views
from exam.models import examType
from django.contrib.auth import views as auth_views

app_name = 'exam'


urlpatterns = [
# /subject/
    url(r'^$', views.index, name='index'),
 	url(r'^subjects/(?P<exam_id>\d+)/$', views.subject_list, name='subject_list'),
 	url(r'^chapters/(?P<subject_id>\d+)/$', views.chapter_list, name='chapter_list'),
 	url(r'^tasks/(?P<chapter_id>\d+)/$', views.problem_list, name='problem_list'),
 	url('^', include('django.contrib.auth.urls'), {'extra_context':{"exams":examType.objects.all()}}),
 	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^logout/$', auth_views.logout, name='logout'), 	

] 

