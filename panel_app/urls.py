from django.urls import path
from panel_app.views.dashboard import DashboardTV 

urlpatterns = [
    path('', DashboardTV.as_view(), name='dashboard_panel'),
]
