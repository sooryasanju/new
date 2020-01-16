from django.urls import path
from . import views

urlpatterns = [
    path('',views.hrget_home.as_view(),name='hrhome'),
    path('studentregister', views.get_register, name='studentregister'),
    path('trainerregister', views.get_trainer, name='trainerregister'),
    path('studentdisplay', views.display_student, name='displaystudent'),
    path('editstudentdata1/<int:pk>', views.StudentUpdate.as_view(), name='editstudentdata'),
    path('deletestudentdata1/<int:pk>', views.StudentDelete.as_view(), name='deletestudentdata'),
    path('displaytrainer', views.TrainerList.as_view(), name='displaytrainer'),
    path('editdata1/<int:pk>', views.TrainerUpdate.as_view(), name='editdata'),
    path('deletedata1/<int:pk>', views.TrainerDelete.as_view(), name='deletedata'),
    path('timetable',views.timetable,name='timetable'),
    path('placement',views.add_jobs,name='placement'),
    path('joblist',views.List_jobs.as_view(),name='joblist'),
    path('hrlogout', views.hrlogout, name='hrlogout'),
]
