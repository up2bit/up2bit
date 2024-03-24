from django.urls import path
from coin import views

urlpatterns = [
    path('favorite_coin/', views.CoinListView.as_view(), name='favorite-coin'),
]