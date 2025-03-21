from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)  # This provides all CRUD endpoints

urlpatterns = [
    path('', include(router.urls)),  # API root for all course-related endpoints
]
