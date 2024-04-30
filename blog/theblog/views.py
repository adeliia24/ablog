from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import  generic

# Create your views here.
def main(request):
    return render(request, 'main.html')


class UserRegistrView(generic.CreateView):
    model = User
    template_name = 'registrate.html'



