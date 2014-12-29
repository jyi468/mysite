from django.conf.urls import patterns, url

from medical import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^$', 'mysite.medical.views.home', name='social'),
)