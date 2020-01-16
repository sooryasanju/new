from django.urls import path
from . import views

urlpatterns = [
    path('',views.trainerget_home.as_view(),name='trainerhome'),
    path('studentdetails',views.student_display, name='studentdetails'),
    path('viewfeedback',views.viewstudentfeedback,name='viewfeedback'),
    path('addcomments/<int:pk>',views.AddComment.as_view(),name='addcomments'),
    path('trainerlogout', views.trainerlogout, name='trainerlogout'),

]
