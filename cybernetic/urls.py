from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render
from cybernetic.views import Index, my_view
from cybernetic import views

urlpatterns = patterns('',
	# ex: /polls/
    url(r'^$', Index.as_view(), name='index'),
    url(r'^mine/', views.my_view, name='myview'),    
)