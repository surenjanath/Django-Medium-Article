"""Article URL Configuration
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('add', views.addFeedbackItem, name = 'Add'),
]
