"""
URL configuration for accounting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from colossal import views

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path("grant/", views.grant),
    path("budget/", views.budget),
    path("donor/", views.donor),
    path("funding/", views.funding),
    path("incomestatement/", views.incomeStatement),
    path("irsfilling/", views.irsFilling),
]
