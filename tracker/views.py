from django.shortcuts import render
from .models import Tracker
# Create your views here.

def get_tracker(request):
    trackers = Tracker.objects.all()
    context = {
        'tracker': trackers
    }
    return render(request, "tracker/tracker.html", context)


def add_trade(request):
    return render(request, "tracker/add_trade.html")
