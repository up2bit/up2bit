from coin import views
from django.urls import path

from coin.views import *

urlpatterns = [
    path('create_coin/', views.CoinCreateView.as_view(), name='create-coin'),
    path('list_of_coins/', views.CoinListView.as_view(), name='list-of-coins'),
    path('delete_coin/', views.CoinDeleteView.as_view(), name='delete-coin'),
]
