from django.shortcuts import render
from .models import Form
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, "index.html")

