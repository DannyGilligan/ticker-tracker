from django.shortcuts import render, redirect
from .models import Tracker
# Create your views here.

def get_tracker(request):
    trackers = Tracker.objects.all()
    context = {
        'tracker': trackers
    }
    return render(request, 'tracker/tracker.html', context)

def add_trade(request):
    if request.method == 'POST':
        status = request.POST.get('trade_status')
        ticker = request.POST.get('trade_ticker')
        position = request.POST.get('trade_position')
        date_opened = request.POST.get('trade_date_opened')
        amount_traded = request.POST.get('trade_amount')
        opening_price = request.POST.get('trade_opening_price')
        Tracker.objects.create(status=status, ticker=ticker, position=position, date_opened=date_opened, amount_traded=amount_traded, opening_price=opening_price)
        
        return redirect('get_tracker')
    return render(request, 'tracker/add_trade.html')
