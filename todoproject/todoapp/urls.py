
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.Tasklistviews.as_view(),name='cbvindex'),
    path('cbvdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.Taskupdateviews.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),
]
