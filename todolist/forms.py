from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Task



class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)


class DateInput(forms.widgets.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_date', 'tags', 'priority', 'completed')
        widgets = {
            'due_date': DateInput(),
        }