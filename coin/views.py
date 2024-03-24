from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from coin.forms import CoinForm
from coin.models import Coin


class CoinCreateView(LoginRequiredMixin, CreateView):
    template_name = 'coin/create_coin.html'
    model = Coin
    form_class = CoinForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):

        if form.is_valid():
            new_coin = form.save()
            get_message = f'A fost adaugata o noua moneda cu pretul : {new_coin.price}'

        return redirect('login')


class CoinListView(LoginRequiredMixin, ListView):
    template_name = 'coin/list_of_coins.html'
    model = Coin
    context_object_name = 'all_coins'


class CoinDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'coin/delete_coin.html'
    model = Coin
    success_url = reverse_lazy('list-of-coins')
