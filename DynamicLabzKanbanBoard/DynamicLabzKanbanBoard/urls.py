from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('create-task', create_task, name='create-task'),
    path('update-task', update_task, name='update-task')
]
