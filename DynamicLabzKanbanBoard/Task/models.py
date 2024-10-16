from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Back Log', 'Back Log'),
        ('On Hold', 'On Hold'),
        ('In Progress', 'In Progress'),
        ('Testing (Client)', 'Testing (Client)'),
        ('Deployed', 'Deployed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    client_work = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
