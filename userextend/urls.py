from django.urls import path
from userextend import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('logout1/', views.logout_view, name='logout1'),
]