from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shows, name='inicio'),
    path('shows/', views.shows, name='shows'),
    path('shows/new/', views.create_show, name='create_show'),
    path('shows/new/add_show/', views.add_show, name='add_show'),
    path('shows/<show_id>/', views.tv_show, name='tv_show'),
    path('shows/<show_id>/edit/', views.edit_show, name='edit_show'),
    path('shows/<show_id>/update/', views.update_show, name='update_show'),
    path('shows/<show_id>/delete/', views.del_show, name='del_show'),
    ]