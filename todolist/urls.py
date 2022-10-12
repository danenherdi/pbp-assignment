from django.urls import path
from todolist.views import add_task_ajax, show_todolist, register_todolist, login_user_todolist, logout_user_todolist, create_task, show_todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('register/', register_todolist, name='register'),
    path('login/', login_user_todolist, name='login'),
    path('logout/', logout_user_todolist, name='logout'),
    path('create-task', create_task, name='create_task'),
    path('add/', add_task_ajax, name='add_task_ajax')
]