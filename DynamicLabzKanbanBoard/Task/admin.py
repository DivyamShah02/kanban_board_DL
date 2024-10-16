from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'client_work', 'date')
    list_filter = ('status', 'client_work', 'date')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
