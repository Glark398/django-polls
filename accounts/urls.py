from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/cadastrar', views.AccountCreateView.as_view(), name='signup'),
    ]
