"""apidjango URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^question/$', 'askquestions.views.index', name='questions'),
    url(r'^question/(?P<question_id>\d+)/$', 'askquestions.views.question_detail', name='question_detail'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^question/create/$', 'askquestions.views.question_create', name='question_create'),
    url(r'^question/edit/(?P<question_id>\d+)/$', 'askquestions.views.question_edit', name='question_edit'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'apidjango.views.login_page', name='login'),
    url(r'^$', 'apidjango.views.homepage', name='homepage'),
    url(r'^logout/$', 'apidjango.views.logout_view', name='logout'),

]
