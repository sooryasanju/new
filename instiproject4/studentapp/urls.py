from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentget_home.as_view(),name='studenthome'),
    path('stuprofile',views.view_profile,name='stuprofile'),
    path('editprofile/<int:pk>',views.ProfileUpdate.as_view(),name='editprofile'),
    path('studentfeedback', views.StudentFeedback.as_view(), name='studentfeedback'),
    path('staffdetails', views.StaffDetails.as_view(), name='stafdetail'),
    path('displaycomment',views.displaycomments,name='displaycomment'),
    path('studentlogout', views.studentlogout, name='studentlogout'),


]
