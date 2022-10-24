from django.urls import path

from core.payment import views

app_name = 'payments'
urlpatterns = [
    path('payments', views.payment, name='payments')
]