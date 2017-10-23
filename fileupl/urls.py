from django.conf.urls import url, include
from upload import views

urlpatterns = [

    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),

]
