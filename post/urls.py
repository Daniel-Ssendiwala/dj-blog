from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index, name ='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('post_create/',views.post_create,name='create'),
    path('post_create/post_process',views.post_process,name='process'),
]