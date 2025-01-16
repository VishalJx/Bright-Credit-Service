from celery import shared_task
from .models import User

@shared_task
def calculate_credit_score(user_id):
    # Calculate credit score based on CSV logic
    user = User.objects.get(id=user_id)
    # Assuming logic calculates the score
    user.credit_score = 700  # Placeholder
    user.save()
