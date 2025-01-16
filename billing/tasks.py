from celery import shared_task
from .views import BillingCronJob
from datetime import date, timedelta
from .models import Billing
from loans.models import Loan


@shared_task
def process_billing():
    view = BillingCronJob()
    view.post(None)

@shared_task
def run_billing_cycle():
    today = date.today()
    loans = Loan.objects.all()
    for loan in loans:
        next_billing_date = loan.disbursement_date + timedelta(days=30)
        if today >= next_billing_date:
            due_date = next_billing_date + timedelta(days=15)
            min_due = (loan.amount * 0.03) + (loan.amount * loan.interest_rate / 365 * 30)
            Billing.objects.create(
                loan=loan, billing_date=next_billing_date, due_date=due_date, min_due=min_due
            )