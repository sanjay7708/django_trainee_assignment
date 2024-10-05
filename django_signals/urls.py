from django.urls import path
from .views import trigger_signal

urlpatterns = [
    path('trigger-signal/', trigger_signal, name='trigger_signal'),
]
