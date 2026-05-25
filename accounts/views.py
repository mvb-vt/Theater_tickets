from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model, login, logout
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import AppUserCreationForm, ProfileForm
from accounts.models import Profile

UserModel = get_user_model()

class HomeView(TemplateView):
    template_name = 'common/home.html'

class TicketsView(TemplateView):
    template_name = 'tickets/tickets.html'


class ProgramsView(TemplateView):
    template_name = 'tickets/programs.html'


class NewsView(TemplateView):
    template_name = 'tickets/news.html'


class ContactView(TemplateView):
    template_name = 'tickets/contact.html'


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/profile-register.html'
    success_url = reverse_lazy('profile edit')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-detail.html'
    context_object_name = 'profile'

    def get_object(self, *args, **kwargs):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-edit.html'

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse_lazy('profile details')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)
