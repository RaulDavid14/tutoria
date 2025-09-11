from django.urls import path 
from catalogos_app.views.licenciatura import LicenciaturaView

urlpatterns = [
    path('licenciatura', LicenciaturaView.as_view(), name='licenciatura_index'),
]