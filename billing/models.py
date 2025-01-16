from django.db import models
from loans.models import Loan

class Billing(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    billing_date = models.DateField()
    due_date = models.DateField()
    min_due = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
