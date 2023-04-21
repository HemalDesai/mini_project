from django.urls import path
from . import views

# app_name = "newapp"
urlpatterns = [
    path('', views.LNMfood_home, name='LNMfood_home'),
    path('view_blog_food)', views.view_blog_food, name='view_blog_food'),
    path('insert_blog_food/', views.insert_blog_food, name='insert_blog_food'),
    path('delete_blog/<int:id>', views.delete_blog, name= 'delete_blog')
]