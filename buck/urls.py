from django.conf.urls import url                    # !Exclude include ... No need.
from . import views                                 # Add views.py @current dir. (.)
# from django.contrib import admin                  # Del admin

urlpatterns = [
    url(r'^buck/$', views.bucket, name='bucket'),
]
