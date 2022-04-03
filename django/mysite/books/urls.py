"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

app_name = 'books'
# url 대신 re_path 사용
urlpatterns = [
    # ex: /polls/
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add/$', views.add, name='add'),
    re_path(r'^delBook/$', views.delBook, name='delBook'),
    # # ex: /polls/5/
    # re_path(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]