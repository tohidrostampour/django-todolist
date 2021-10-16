from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager



class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        Medium = 2, 'Medium'
        High = 3, 'High'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    priority = models.PositiveIntegerField(choices=Priority.choices, default=Priority.LOW)

    class Meta:
        ordering = ('priority',)

    def __str__(self) -> str:
        return self.title
