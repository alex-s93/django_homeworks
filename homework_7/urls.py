from django.urls import path
from homework_7.views import greeting

urlpatterns = [
    path('', greeting, name='greeting')
]