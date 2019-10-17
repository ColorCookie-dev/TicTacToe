from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpRedirect
from .admin import UserCreationForm
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def AccSettings(request):
    if request.user.is_authenticated():
        return HttpRedirect(reverse_lazy('login'))
    return render(request, 'accounts/AccSettings.html')
