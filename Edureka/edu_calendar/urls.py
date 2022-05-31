from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:year>/<int:month>/', views.index),
    path('contactus/', views.contact_us),
    path('contact_us/', views.ContactUs.as_view()),
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('student/', views.StudentCreate.as_view()),
]

