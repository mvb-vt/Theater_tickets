from django.urls import path

from accounts.views import HomeView, AppUserRegisterView, LoginUserView, LogoutUserView, ProfileDetailView, \
    ProfileEditView, ProfileDeleteView, TicketsView, ProgramsView, NewsView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tickets/', TicketsView.as_view(), name='tickets'),
    path('programs/', ProgramsView.as_view(), name='programs'),
    path('news/', NewsView.as_view(), name='news'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('profile-details/', ProfileDetailView.as_view(), name='profile details'),
    path('profile-edit/', ProfileEditView.as_view(), name='profile edit'),
    path('profile-delete/', ProfileDeleteView.as_view(), name='profile delete'),
]
