from django.shortcuts import render
from django.views.generic import DetailView, FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegisterUsers(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context