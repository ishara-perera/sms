from django.urls import path

from scts import views

urlpatterns = [
    path('students/create/', views.create_student, name="create_student"),
    path('students/get/<int:pk>', views.get_student, name="get_student"),
    path('students/', views.get_students_all, name="get_student_all"),
    path('students/delete/<int:pk>', views.delete_student, name="delete_student"),
    path('students/update/<int:pk>/', views.update_student, name='update_student'),

    path('classrooms/create/', views.create_classroom, name="create_classroom"),
    path('classrooms/', views.get_classrooms_all, name="get_classrooms_all"),
    path('classrooms/get/<int:pk>', views.get_classroom, name="get_classroom"),
    path('classrooms/delete/<int:pk>', views.delete_classroom, name="get_classroom"),
    path('classrooms/update/<int:pk>', views.update_classroom, name="get_classroom"),
]
