from django import forms
from .models import Tracker


class TradeForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['status', 'ticker', 'position', 'date_opened', 'amount_traded', 'opening_price']
        widgets = {
            'date_opened': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'date_closed': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }

class EditTradeForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['status', 'ticker', 'position', 'date_opened', 'amount_traded', 'opening_price', 'closing_price', 'date_closed', 'profit_loss', 'result']
        widgets = {
            'date_opened': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'date_closed': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }
