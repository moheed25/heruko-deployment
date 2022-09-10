from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="/"),
    path('student-view/<str:pk>/',views.studentView,name="studentView"),
    path('add-student/',views.studentAdd,name="studentAdd"),
    path('update-student/<str:pk>/',views.studentUpdate,name="studentUpdate"),
    path('delete-student/<str:pk>/',views.studentDelete,name="studentDelete"),
]