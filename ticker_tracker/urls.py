"""ticker_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracker.views import get_tracker, add_trade, edit_trade, delete_trade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_tracker, name='get_tracker'),
    path('add_trade', add_trade, name='add_trade'),
    path('edit_trade/<ticker_id>', edit_trade, name='edit_trade'),
    path('delete_trade/<ticker_id>', delete_trade, name='delete_trade'),
]
