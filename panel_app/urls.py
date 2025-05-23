from django.urls import path
from panel_app.views.dashboard import DashboardTV 
from panel_app.views.catalogos import CatalogosTV
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path('', DashboardTV.as_view(), name='dashboard_panel'),
    path('catalogos/', CatalogosTV.as_view(), name='panel_catalogos'),
    path('panel/logout', LogoutView.as_view(next_page='panel_login'), name='panel_logout'),
]