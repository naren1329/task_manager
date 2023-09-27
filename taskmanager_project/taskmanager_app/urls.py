"""
URL configuration for taskmanager_project project.

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
from django.urls import path
from . import views
urlpatterns = [
    path('',views.task_homepage,name='task_home'),
    path('register/',views.register,name="register"),
    path('login/',views.reg_login_fun,name='reg_log'),
    path('taskhome/',views.task_homepage,name='task_home'),
    path('forgot/',views.forgot_fun,name='forgot'),
    path('tasks/',views.add_task,name='tasks'),
    path('dashboard/',views.dashboard,name='alltask'),
    path('<int:id>/delete',views.delete_task,name='delete'),
    path('update/<int:id>/',views.update_task,name='update')
]
