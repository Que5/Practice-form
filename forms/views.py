from django.shortcuts import render
from django.views.generic import DetailView
from .models import Form
from .forms import ContactForm

# Create your views here.

class FormDetail(DetailView):
    model = Form
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context

