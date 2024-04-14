from django.shortcuts import render

def activity_list(request):
    return render(request, 'tripinspiration/activity_list.html', {})
