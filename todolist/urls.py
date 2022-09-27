from django.urls import path
from todolist.views import show_todolist, register_todolist, login_user_todolist, logout_user_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register_todolist, name='register'),
    path('login/', login_user_todolist, name='login'),
    path('logout/', logout_user_todolist, name='logout'),
    path('create-task', create_task, name='create_task'),
]