
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Payment(models.Model):
    """
    Models to payment
    Args:
        models (_type_): _description_
    """
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(editable=False)
    payment_ammount = models.DecimalField(max_digits=8, decimal_places=4)
    provider = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    company = models.CharField(max_length=20)
    new_value_payment = models.DecimalField(max_digits=8, decimal_places=4, editable=False)



    def __str__(self) -> str:
        return f'{self.provider} - {self.company}'
    
    def save(self):
        from datetime import datetime, timedelta
        d = timedelta(days=30)

        if not self.id:
            self.due_date = datetime.now() + d
            super(Payment, self).save()

    