from django.shortcuts import render, redirect
from .models import Tracker
from .forms import TradeForm

# Create your views here.

# View for the main tracker that will render all ticker related objects (opening price, closing price etc).

def get_tracker(request):
    trackers = Tracker.objects.all()
    context = {
        'tracker': trackers
    }
    return render(request, 'tracker/tracker.html', context)


# View for the Add Trade form that will allow user to add a new trade with all related parameters, and then redirect the user back to the Tracker once submitted.

def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_tracker')
    form = TradeForm()
    context = {
        'form': form
    }
    return render(request, 'tracker/add_trade.html', context)

# View to Edit trades, this will render the edit_trade.html page

def edit_trade(request, ticker_id):
    return render(request, 'tracker/edit_trade.html')