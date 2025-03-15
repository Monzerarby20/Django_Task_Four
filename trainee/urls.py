from django.urls import path
from .views import (
    TraineeListView,
    TraineeCreateView,
    TraineeUpdateView,
    TraineeDeleteView,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('trainees/', TraineeListView.as_view(), name='trainee_list'),
    path('trainees/add/', TraineeCreateView.as_view(), name='add_trainee'),
    path('trainees/<int:pk>/edit/', TraineeUpdateView.as_view(), name='update_trainee'),
    path('trainees/<int:pk>/delete/', TraineeDeleteView.as_view(), name='delete_trainee'),
]
