from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class LicenciaturaView(TemplateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'catalogos/genero.html'
    login_url = 'panel_login'

    def test_func(self):
        return super().test_func()
    