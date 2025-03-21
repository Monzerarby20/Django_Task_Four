from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_courses(request):
    return redirect('/course/')  # Redirect root URL to /course/

urlpatterns = [
    path('', redirect_to_courses),  # Redirect root URL to course app
    path('admin/', admin.site.urls),
    path('trainee/', include('trainee.urls')),
    path('course/', include('course.urls')),
]
