from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),
    path('profile/<int:pk>', views.user_profile, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
    path('reset/', views.reset_password, name="reset"),
    path('emailcode/', views.email_code, name="email_code"),
]
