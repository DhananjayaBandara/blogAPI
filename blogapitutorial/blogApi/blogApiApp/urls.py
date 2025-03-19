from django.urls import path
from . import views      # . represents the current folder

urlpatterns=[
    path('',views.index),
    path('get-all-posts/',views.GetAllPosts)
]