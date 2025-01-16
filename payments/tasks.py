from celery import shared_task
from .models import Payment
from loans.models import Loan

@shared_task
def process_payment(payment_id):
    """
    Processes a payment asynchronously and updates the loan balance.
    """
    try:
        payment = Payment.objects.get(id=payment_id)
        loan = payment.loan
        loan.amount -= payment.amount
        loan.save()
        print(f"Payment of {payment.amount} processed for Loan ID: {loan.id}")
    except Payment.DoesNotExist:
        print(f"Payment ID {payment_id} not found.")
