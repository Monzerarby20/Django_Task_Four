from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ListTraineeView, 
    AddTraineeView,  
    UpdateTraineeView, 
    DeleteTraineeView, 
    track_update, 
    TrackViewSet
)

router = DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='track')

urlpatterns = [
    path('list/', ListTraineeView.as_view(), name='list-trainee'),  
    path('add/', AddTraineeView.as_view(), name='add-trainee'),  
    path('update/<int:pk>/', UpdateTraineeView.as_view(), name='update-trainee'),  
    path('delete/<int:pk>/', DeleteTraineeView.as_view(), name='delete-trainee'),  
    path('track/update/', track_update, name='track-update'),  
] + router.urls
