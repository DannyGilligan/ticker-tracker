from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracker
from .forms import TradeForm
from .forms import EditTradeForm

# Create your views here.

# View for the main tracker that will render all ticker related objects (opening price, closing price etc).

def get_tracker(request):
    trackers = Tracker.objects.all()
    context = {
        'tracker': trackers
    }
    return render(request, 'tracker/tracker.html', context)



# View for the Add Trade form that will allow user to add a new trade with all related parameters, and then redirect the user back to the Tracker once submitted. The view pulls in the TradeForm that has an abbreviated number of fields that are confined only to those necessary for opening a new trade (to improve the UX)

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



# View to Edit trades, this will render the edit_trade.html page, it also used the EditTradeForm to show all editable fields (as opposed to only those fields necessary to add a new trade in TradeForm)

def edit_trade(request, ticker_id):
    ticker = get_object_or_404(Tracker, id =ticker_id)
    if request.method == 'POST':
        form = EditTradeForm(request.POST, instance=ticker)
        if form.is_valid():
            form.save()
            return redirect('get_tracker')
    form = EditTradeForm(instance=ticker)
    context = {
        'form': form
    }
    return render(request, 'tracker/edit_trade.html', context)