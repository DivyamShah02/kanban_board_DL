#####
# Divyam
# Navkar@108
#####

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Task.models import Task
from django.utils import timezone

def home(request):
    Pending = Task.objects.filter(status='Pending')
    Back_Log = Task.objects.filter(status='Back Log')
    On_Hold = Task.objects.filter(status='On Hold')
    In_Progress = Task.objects.filter(status='In Progress')
    Testing_Client = Task.objects.filter(status='Testing (Client)')
    Deployed = Task.objects.filter(status='Deployed')

    data = {
        'Pending':Pending,
        'Back_Log':Back_Log,
        'On_Hold':On_Hold,
        'In_Progress':In_Progress,
        'Testing_Client':Testing_Client,
        'Deployed':Deployed,
        'len_Pending':len(Pending),
        'len_Back_Log':len(Back_Log),
        'len_On_Hold':len(On_Hold),
        'len_In_Progress':len(In_Progress),
        'len_Testing_Client':len(Testing_Client),
        'len_Deployed':len(Deployed),
    }
    return render(request, 'index.html', data)

def create_task(request):
    if request.method == 'POST':
        # Get the data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        client_work = request.POST.get('client_work', 'false') == 'true'  # Convert string to boolean

        # Validate data (you can add more validation as needed)
        if not title or not status:
            return JsonResponse({'error': 'Title and Status are required fields'}, status=400)

        # Create and save the task
        task = Task(
            title=title,
            description=description,
            status=status,
            client_work=client_work,
            date=timezone.now()  # This will take the current time automatically
        )
        task.save()

        # Return a success response
        return JsonResponse({'status':True,'message': 'Task created successfully', 'task_id': task.id}, status=201)
    else:
        return JsonResponse({'status':False,'error': 'Invalid request method'}, status=405)
