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
    url(r'^login/$', 'apidjango.views.login_page', name='login'),
    url(r'^$', 'apidjango.views.homepage', name='homepage'),
    url(r'^logout/$', 'apidjango.views.logout_view', name='logout'),
    url(r'^generic/$', 'apis.views.package_generic', name='generic'),
    url(r'^generic/create/$', 'apis.views.generic_create', name='generic_create'),
    url(r'^generic/edit/(?P<package_id>\d+)/$', 'apis.views.generic_edit', name='generic_edit'),
    url(r'^packages/genericedu/$', 'apis.views.package_generic_edu', name='generic_edu'),
    url(r'^packages/genericedu/create/$', 'apis.views.generic_edu_create', name='generic_edu_create'),
    url(r'^packages/genericedu/edit/(?P<package_id>\d+)/$', 'apis.views.generic_edu_edit', name='generic_edu_edit'),
    url(r'^packages/cinnamon/$', 'apis.views.package_cinnamon', name='package_cinnamon'),
    url(r'^packages/cinnamon/create/$', 'apis.views.package_cinnamon_create', name='package_cinnamon_create'),
    url(r'^packages/cinnamon/edit/(?P<package_id>\d+)/$', 'apis.views.package_cinnamon_edit', name='package_cinnamon_edit'),
    url(r'^packages/cinnamon/edu/$', 'apis.views.package_cinnamon_edu', name='package_cinnamon_edu'),
    url(r'^packages/cinnamon/edu/create/$', 'apis.views.package_cinnamon_edu_create', name='package_cinnamon_edu_create'),
    url(r'^packages/cinnamon/edu/edit/(?P<package_id>\d+)/$', 'apis.views.package_cinnamon_edu_edit', name='package_cinnamon_edu_edit'),
    url(r'^packages/mate/$', 'apis.views.package_mate', name='package_mate'),
    url(r'^packages/mate/create/$', 'apis.views.package_mate_create', name='package_mate_create'),
    url(r'^packages/mate/edit/(?P<package_id>\d+)/$', 'apis.views.package_mate_edit', name='package_mate_edit'),
    url(r'^packages/mate/edu/$', 'apis.views.package_mate_edu', name='package_mate_edu'),
    url(r'^packages/mate/edu/create/$', 'apis.views.package_mate_edu_create', name='package_mate_edu_create'),
    url(r'^packages/mate/edu/edit/(?P<package_id>\d+)/$', 'apis.views.package_mate_edu_edit', name='package_mate_edu_edit')



]
