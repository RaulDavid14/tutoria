from django.views.generic import CreateView
from tutoria_app.forms.sesiones import SesionesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

class SesionesCV(LoginRequiredMixin, CreateView):
    template_name = 'sesiones/index.html'
    form_class = SesionesForm

