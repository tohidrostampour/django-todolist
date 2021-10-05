from bootstrap_datepicker_plus import DateTimePickerInput
from django.db.models import query
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskCreateForm




class UserLoginView(LoginView):
    template_name = 'todolist/login.html'
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
        return redirect('todolist:user-login')


class TaskList(ListView):
    model = Task
    # Whatever the model is the django will look for //modelname_list.html you can change in
    template_name = 'todolist/task_list.html'
    # if you don't assign anything it'll be object_list in templates
    context_object_name = 'tasks'

    def get_queryset(self):
            queryset = super(TaskList, self).get_queryset()
            try:
                queryset = queryset.filter(user=self.request.user)
            except:
                return None
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskCreateForm()
        return context


class TaskCreate(FormView):
    model = Task 
    form_class = TaskCreateForm
    template_name = 'todolist/task_list.html'
    success_url = reverse_lazy('todolist:tasks')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return super().post(request, *args, **kwargs)
    
    success_url = reverse_lazy('todolist:tasks')


class TaskListCreateView(View):
    def get(self, request, *args, **kwargs):
        view = TaskList.as_view()
        return view(request,*args, **kwargs)

    def post(self,request, *args, **kwargs):
        view = TaskCreate.as_view()
        return view(request,*args, **kwargs)


class TaskDetail(DetailView):
    model = Task
    template_name = 'todolist/task_detail.html'
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'todolist/task_update.html'
    fields = ('title', 'due_date', 'completed', 'category', 'priority')
    success_url = reverse_lazy('todolist:tasks')

    def get_form(self):
        form = super().get_form()
        form.fields['due_date'].widget = DateTimePickerInput()
        return form


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todolist:tasks')
