from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from coin.models import Coin


class PortfolioListView(LoginRequiredMixin, ListView):
    template_name = 'portfolio/favorite_coin.html'
    model = Coin
    context_object_name = 'all_coins'
