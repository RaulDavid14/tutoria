from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class IndexHomeAV(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = 'login'
    success_url = reverse_lazy('home')