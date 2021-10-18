from bootstrap_datepicker_plus import DateTimePickerInput
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

from taggit.models import Tag

from .models import Task
from .forms import TaskCreateForm, TodoForm
from .permissions import HasPerm



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


class TaskCreate(LoginRequiredMixin ,FormView):
    model = Task 
    form_class = TaskCreateForm
    template_name = 'todolist/task_list.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return super().post(request, *args, **kwargs)
    
    success_url = reverse_lazy('todolist:tasks')


class TaskListCreateView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    def get(self, request, *args, **kwargs):
        view = TaskList.as_view()
        return view(request,*args, **kwargs)

    def post(self,request, *args, **kwargs):
        view = TaskCreate.as_view()
        return view(request,*args, **kwargs)


class TaskDetail(LoginRequiredMixin, HasPerm,DetailView):
    login_url = '/accounts/login/'
    model = Task
    template_name = 'todolist/task_detail.html'
    context_object_name = 'task'
    
    def get(self, request, *args, **kwargs):
        return HasPerm.has_perm(self, request, *args, **kwargs)


class TaskUpdate(LoginRequiredMixin, HasPerm, UpdateView):
    login_url = '/accounts/login/'
    model = Task
    form_class = TodoForm
    template_name = 'todolist/task_update.html'
    # fields = ('title', 'due_date', 'tags','priority', 'completed')
    success_url = reverse_lazy('todolist:tasks')

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['due_date'].widget = DateTimePickerInput()
    #     return form
    def get(self, request, *args, **kwargs):
        return HasPerm.has_perm(self, request, *args, **kwargs)



class TaskDelete(LoginRequiredMixin, HasPerm, DeleteView):
    login_url = '/accounts/login/'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todolist:tasks')

    def get(self, request, *args, **kwargs):
        return HasPerm.has_perm(self, request, *args, **kwargs)


class TaggedTasks(LoginRequiredMixin, HasPerm, ListView):
    login_url = '/accounts/login/'
    look_up = 'slug'
    context_object_name = 'tagged_tasks'
    template_name = 'todolist/tagged_tasks.html'

    def get_queryset(self):
        try:
            queryset = Task.objects.filter(tags__slug__iexact=self.kwargs['slug'])
        except:
            return None
        return queryset