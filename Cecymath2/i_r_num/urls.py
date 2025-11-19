from django.urls import path
from . import views

urlpatterns =[
    path("", views.home. name="i_r_num_home"),
]