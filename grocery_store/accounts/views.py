from .forms import UserCreate
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from groceries.models import Grocery_store
from django.core.mail import send_mail
import os
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = UserCreate
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Grocery_StoreView(ListView):
    model = Grocery_store
    template_name = 'groceries/home.html'


def home(request):
    send_mail('Hello from Grocery store app',
              os.environ.get('ADMINS'),
              [os.environ.get('NotifyEmail')],
              fail_silently=False)
    return render(request, 'home.html')