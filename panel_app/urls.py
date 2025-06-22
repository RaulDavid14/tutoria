from django.urls import path
from panel_app.views.dashboard import DashboardTV 
from panel_app.views.catalogos import CatalogosTV
from django.contrib.auth.views import  LogoutView
from panel_app.views.register_docente import RegisterDocenteCV


urlpatterns = [
    path('', DashboardTV.as_view(), name='dashboard_panel'),
    path('catalogos/', CatalogosTV.as_view(), name='panel_catalogos'),
    path('logout', LogoutView.as_view(next_page='panel_login'), name='panel_logout'),
    path('register/academico', RegisterDocenteCV.as_view(), name='register_docente'),
]