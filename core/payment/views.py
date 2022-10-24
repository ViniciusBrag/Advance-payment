
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def payment(request):
    return render(request, 'payment/payment.html')
