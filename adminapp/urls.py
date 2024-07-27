# adminapp/urls.py

from django.urls import path
from .views import export_data

urlpatterns = [
    path('export-data/', export_data, name='export_data'),
]
