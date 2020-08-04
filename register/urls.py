from django.urls import path, include

from django.contrib.auth import views as auth_views


from . import views
app_name = 'register'
urlpatterns = [
    path('', views.membership, name='membership'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.create_account_page, name='create_account_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),








]