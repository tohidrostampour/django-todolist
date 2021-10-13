from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('user-login')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:tasks')
        else:
            messages.error(request, 'Wrong password or username')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user-login')
