"""
URL configuration for success_tracker_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# success_tracker_project/urls.py
# success_tracker_project/urls.py
from django.contrib import admin
from django.urls import path, include
from success_tracker.views import home, dashboard, task_list, complete_task, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/<int:task_id>/complete/', complete_task, name='complete_task'),
    path('register/', register, name='register'),  # Add this line for registration
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    # Add other URL patterns as needed
]

