from django.db import models
from users.models import User

class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_period = models.IntegerField()  # in months
    disbursement_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
