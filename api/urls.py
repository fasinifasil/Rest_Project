from django.urls import path
from . import  views
urlpatterns = [
    path('',views.apiOverview,name="api-oberview"),
    path('tasklist/',views.tasklist,name="api-tasklist"),
    path('taskDetail/<str:pk>/',views.taskDetail,name="api-taskdetail"),
    path('taskCreate/',views.taskCreate,name="api-taskCreate"),
    path('taskUpdate/<str:pk>/',views.taskUpdate,name="api-taskupdate"),
    path('taskDelete/<str:pk>/',views.taskDelete,name="api-taskdelete")
]