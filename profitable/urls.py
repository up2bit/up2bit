from django.urls import path
from coin import views

urlpatterns = [
    path('profitable_coin/', views.ProfitableListView.as_view(), name='profitable-coin'),
]