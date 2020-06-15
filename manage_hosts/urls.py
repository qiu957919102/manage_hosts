"""manage_hosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from manageHost import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('host/', views.host),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view(),name='login'),
    re_path('del-(?P<nid>\d+)/', views.delHost),
    path('add/', views.addHost.as_view(),name='add'),
    re_path('edit-(?P<nid>\d+)/', views.EditHost.as_view()),
    re_path('detail-(?P<nid>\d+)/', views.detail),
    path(r'', views.base),
]
