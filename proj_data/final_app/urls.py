"""proj_data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('view_admin', views.view_admin, name='view_admin'),
    path('add_admin', views.add_admin, name='add_admin'),
    path('remove_admin', views.remove_admin, name='remove_admin'),
    path('remove_admin/<int:stds_id>', views.remove_admin, name='remove_admin'),
    path('viewequipment', views.viewequipment, name='viewequipment'),
    path('add_equipment', views.add_equipment, name='add_equipment'),
    path('remove_equipment', views.remove_equipment, name='remove_equipment'),
    path('remove_equipment/<int:eqp_id>', views.remove_equipment, name='remove_equipment'),
    path('borrow_equipment', views.borrow_equipment, name='borrow_equipment'),

]
