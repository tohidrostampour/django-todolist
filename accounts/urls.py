from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, UserLoginView, UserLogoutView



urlpatterns = (
    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name='password_reset'),

    path('reset-password-sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset_confirm'),

    path('reset-password-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login')
)