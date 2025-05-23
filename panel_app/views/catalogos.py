from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class CatalogosTV(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'panel/catalogos.html'
    login_url = 'panel_login'

    def test_func(self):
        return self.request.user.is_superuser