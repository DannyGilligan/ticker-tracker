from django.shortcuts import render

# Create your views here.

def get_tracker(request):
    return render(request, "tracker/tracker.html")
