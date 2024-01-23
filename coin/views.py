from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from coin.forms import CoinForm
from coin.models import Coin


class CoinCreateView(LoginRequiredMixin, CreateView):
    template_name = 'coin/create_coin.html'
    model = Coin
    form_class = CoinForm
    success_url = reverse_lazy('home_page')


class CoinListView(LoginRequiredMixin, ListView):
    template_name = 'coin/list_of_coins.html'
    model = Coin
    context_object_name = 'all_coins'


class CoinDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'coin/delete_coin.html'
    model = Coin
    success_url = reverse_lazy('list-of-coins')

