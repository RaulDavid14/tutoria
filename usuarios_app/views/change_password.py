from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/change_password.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.user.cambiar_password = False
        self.request.user.save()
        return response