from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Task



class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)
