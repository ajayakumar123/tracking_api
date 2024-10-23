# tracking/urls.py
from django.urls import path
from .views import TrackNumberView

urlpatterns = [
    path('next-tracking-number/', TrackNumberView.as_view(), name='next_tracking_number'),
]
