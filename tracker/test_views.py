from django.test import TestCase
from .models import Tracker

# Create your tests here.

#These will test the views used in the project. The code for this was taken from the Code Institute LMS (testing forms section)

class TestViews(TestCase):

    def test_get_tracker(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/tracker.html')


    def test_add_trade(self):
        response = self.client.get('/add_trade')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker/add_trade.html')




    
