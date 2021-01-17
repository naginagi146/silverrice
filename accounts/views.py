from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, UserCreationForm, UserUpdateForm
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class Logout(LogoutView):
    template_name = 'registration/logout.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class ProfileView(DetailView):
    model = User
    template_name = "accounts/profile.html"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "accounts/create.html"

    def form_valid(self, form):
            result = super().form_valid(form)
            return result

    def get_success_url(self):
        return reverse_lazy('accounts:login')


class UserUpdateView(LoginRequiredMixin, OnlyYouMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/update.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs={'pk': self.object.pk})

