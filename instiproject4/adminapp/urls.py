from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_home.as_view(),name='home'),
    path('about',views.get_about.as_view(),name='about'),
    path('course',views.CourseList.as_view(),name='course'),
    path('coursedetails',views.get_coursedetail.as_view(),name='coursedetails'),
    path('contact',views.get_contact.as_view(),name='contact'),

]