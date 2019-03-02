from django.urls import path

from . import views
from . import api_views
urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('view/<int:pk>', views.TaskView.as_view(), name='task_view'),
    path('new', views.TaskCreate.as_view(), name='task_new'),
    path('view/<int:pk>', views.TaskView.as_view(), name='task_view'),
    path('edit/<int:pk>', views.TaskUpdate.as_view(), name='task_edit'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),

    ########################### Api Section ##############################
    path('api/task/list', api_views.TaskList.as_view(), name='task_api_list'),
    path('api/taskview/<int:pk>', api_views.TaskDetailView.as_view(), name='task_api_view'),

]