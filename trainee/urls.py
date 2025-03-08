from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),  # تأكد من عدم وجود خطأ هنا
    path('add/', views.add_trainee, name='add_trainee'),
]
