from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

class DashboardTV(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'panel/dashboard.html'
    login_url = 'panel_login'

    def test_func(self):
        return self.request.user.is_superuser
    
        