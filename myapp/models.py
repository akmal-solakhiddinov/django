from django.db import models

# Create your models here.
User = ''


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title