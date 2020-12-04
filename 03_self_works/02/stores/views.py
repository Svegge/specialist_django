from django.views.generic import CreateView, TemplateView
# Create your views here.
from .forms import StoreCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = StoreCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html' 


class HomePageView(TemplateView):
    template_name = 'home.html' 
