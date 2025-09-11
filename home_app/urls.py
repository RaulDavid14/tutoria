from django.urls import path
from .views import IndexHomeAV

urlpatterns = [
    path('', IndexHomeAV.as_view(), name='home'),
]
