from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home_app.urls')),
    path('', include('usuarios_app.urls')),
    path('', include('landing_app.urls')),
]