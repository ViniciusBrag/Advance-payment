from django.contrib.admin import ModelAdmin, register

from core.payment.models import Payment


@register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('issue_date', 'due_date', 'payment_ammount', 'provider', 'company',)