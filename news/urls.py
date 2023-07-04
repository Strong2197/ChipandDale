from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('news/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('menu/', views.menu_detail, name='menu_detail'),
    path('kids/', views.kids_detail, name='kids_detail'),
    path('kids/<int:pk>/edit', views.kids_edit, name='kids_edit'),
    path('kids/new/', views.kids_new, name='kids_new'),
    path('kids/delete/<int:pk>/', views.kids_delete, name='kids_delete'),
    path('menu/<int:pk>/edit', views.menu_edit, name='menu_edit'),
    path('menu/new/', views.menu_new, name='menu_new'),
    path('menu/delete/<int:pk>/', views.menu_delete, name='menu_delete'),
    path('post/<int:pk>/post_add_photo', views.upload, name='post_add_photo'),



]
