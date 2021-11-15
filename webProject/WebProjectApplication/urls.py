from django.urls import path, include
from . import views
from .views import TovarView, RoomView
from django.contrib import admin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('main', views.index, name='index'),
    path('', include('frontend.urls')),

    path('room', RoomView.as_view(), name='room'),
    path('tovar', TovarView.as_view(), name='tovar'),

    path('createbanks', views.createbanks, name='createbanks'),
    path('editbanks/<int:id>/', views.editbanks, name='editbanks'),
    path('deletebanks/<int:id>/', views.deletebanks, name='deletebanks'),

    path('createtovar', views.createtovar, name='createtovar'),
    path('edittovar/<int:id>/', views.edittovar, name='edittovar'),
    path('deletetovar/<int:id>/', views.deletetovar, name='deletetovar'),

    path('createkategory', views.createkategory, name='createkategory'),
    path('editkategory/<int:id>/', views.editkategory, name='editkategory'),
    path('deletekategory/<int:id>/', views.deletekategory, name='deletekategory'),

    path('createnalog', views.createnalog, name='createnalog'),
    path('editnalog/<int:id>/', views.editnalog, name='editnalog'),
    path('deletenalog/<int:id>/', views.deletenalog, name='deletenalog'),

    path('createdvizhenie', views.createdvizhenie, name='createdvizhenie'),
    path('editdvizhenie/<int:id>/', views.editdvizhenie, name='editdvizhenie'),
    path('deletedvizhenie/<int:id>/', views.deletedvizhenie, name='deletedvizhenie'),

    path('createorg', views.createorg, name='createorg'),
    path('editorg/<int:id>/', views.editorg, name='editorg'),
    path('deleteorg/<int:id>/', views.deleteorg, name='deleteorg'),

    path('createnakladnie', views.createnakladnie, name='createnakladnie'),
    path('editnakladnie/<int:id>/', views.editnakladnie, name='editnakladnie'),
    path('deletenakladnie/<int:id>/', views.deletenakladnie, name='deletenakladnie'),

    path('createpodr', views.createpodr, name='createpodr'),
    path('editpodr/<int:id>/', views.editpodr, name='editpodr'),
    path('deletepodr/<int:id>/', views.deletepodr, name='deletepodr'),

    path('createtaks', views.createtaks, name='createtaks'),
    path('edittaks/<int:id>/', views.edittaks, name='edittaks'),
    path('deletetaks/<int:id>/', views.deletetaks, name='deletetaks'),

    path('createost', views.createost, name='createost'),
    path('editost/<int:id>/', views.editost, name='editost'),
    path('deleteost/<int:id>/', views.deleteost, name='deleteost'),

    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]