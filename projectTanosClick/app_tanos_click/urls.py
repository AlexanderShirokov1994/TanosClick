from django.urls import path
from .views import tanos_click_view

urlpatterns = [
    path('', tanos_click_view, name='click')
]
