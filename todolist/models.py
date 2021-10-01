from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'L', 'Low'
        Medium = 'M', 'Medium'
        High = 'H', 'High'

    title = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now())
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    priority = models.CharField(
        max_length=1, choices=Priority.choices, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title
