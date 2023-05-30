from django import forms
from .models import Tracker


class ItemForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [status, ticker, position, date_opened, amount_traded, opening_price]
