from django.urls import path
from .views import TaskList,TaskDetail, TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    #Create Task
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    #update Task
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update-task'),
    #delete Task
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
]