from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    # Add the remaining URL path configurations here
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_items, name='display_menu_items'),

]