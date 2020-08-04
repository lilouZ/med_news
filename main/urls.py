from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.articles, name='articles'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit/<str:pk>/', views.edit_article, name='edit_article'),
    path('delete/<str:pk>/', views.delete_article, name='delete_article'),
    path('<str:pk>/', views.details, name='details'),

    
]