from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Task



class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)


class MyDatePickerInput(DatePickerInput):
    template_name = 'todolist/task_update.html'


class ToDoForm(forms.Form):
    date = forms.DateField(
        widget=MyDatePickerInput(format='%m/%d/%Y')
    )
    class Meta:
        model = Task 
        fields = ('title', 'completed', 'category', 'priority')