from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todolist'),
    path('add', views.todocreate, name='addtodo'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('<int:id>/details/', views.tododetails, name="details"),
    path('<str:pk>/update/', views.todoupdate, name='update'),
    path('login', views.Loginuser, name = "login"),
    path('signup', views.signup_view, name="signup"),
    path('logout', views.Logoutuser, name='logout' )
]
