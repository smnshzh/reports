from django.contrib import admin
from django.urls import path,include
from  .views import *


urlpatterns = [
    path("login",log_in,name="login"),
    path('report',report,name="report" ),
    path('logout',log_out,name='logout')

]
