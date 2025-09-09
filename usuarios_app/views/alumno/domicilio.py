from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios_app.forms.domicilio import DomicilioForm
from django.contrib import messages

class UDomicilioView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'usuarios/datos_generales/domicilio.html'
    form_class = DomicilioForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domicilio'] = context.pop('form')
        return context
    
    def get_object(self):
        return self.request.user.domicilio
     
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    