from django.test import TestCase
from .forms import TradeForm

# Create your tests here.

#These will test the required fields that are needed on the TradeForm in order to add a trade to the tracker. The code for this was taken from the Code Institute LMS (testing forms section)

class TestForms(TestCase):

    def test_trade_status_required(self):
        form = TradeForm({'status': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors.keys())
        self.assertEqual(form.errors['status'][0], 'This field is required.')

    def test_trade_ticker_required(self):
        form = TradeForm({'ticker': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ticker', form.errors.keys())
        self.assertEqual(form.errors['ticker'][0], 'This field is required.')

    def test_trade_position_required(self):
        form = TradeForm({'position': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('position', form.errors.keys())
        self.assertEqual(form.errors['position'][0], 'This field is required.')

    def test_trade_date_opened_required(self):
        form = TradeForm({'date_opened': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date_opened', form.errors.keys())
        self.assertEqual(form.errors['date_opened'][0], 'This field is required.')

    def test_trade_amount_traded_required(self):
        form = TradeForm({'amount_traded': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('amount_traded', form.errors.keys())
        self.assertEqual(form.errors['amount_traded'][0], 'This field is required.')

    def test_trade_opening_price_required(self):
        form = TradeForm({'opening_price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('opening_price', form.errors.keys())
        self.assertEqual(form.errors['opening_price'][0], 'This field is required.')

        


