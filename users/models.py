from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)
    credit_score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
