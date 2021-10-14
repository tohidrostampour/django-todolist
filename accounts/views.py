from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('user-login')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todolist:tasks')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user-login')
