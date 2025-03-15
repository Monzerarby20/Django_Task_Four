from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('add/', CourseCreateView.as_view(), name='add_course'),  # ✅ Matches 'add_course'
    path('edit/<int:pk>/', CourseUpdateView.as_view(), name='update_course'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),
]
