from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView  
from django.views import View

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')  

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')  
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
    
class LogoutView(View):
    def post(self, request, *args, **kwargs):  
        logout(request)  
        return redirect('home')
    

class CustomLoginView(LoginView):
    template_name = 'registration/login.html' 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  
        return super().get(request, *args, **kwargs)


class Custom404View(View):
    def get(self, request, *args, **kwargs):
        return redirect('home')  