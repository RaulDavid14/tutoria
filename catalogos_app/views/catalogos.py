from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView

class CatalogoView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = 'panel_login'
    
    def test_func(self):
        return self.request.user.is_superuser