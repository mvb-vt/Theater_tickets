from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model, login, logout
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

UserModel = get_user_model()

class HomeView(TemplateView):
    template_name = 'common/home.html'

class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('home')