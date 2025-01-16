from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Billing
from loans.models import Loan
from datetime import timedelta, date

class BillingCronJob(APIView):
    def post(self, request):
        today = date.today()
        loans = Loan.objects.all()
        for loan in loans:
            billing_date = loan.disbursement_date + timedelta(days=30)
            if billing_date <= today:
                due_date = billing_date + timedelta(days=15)
                min_due = (loan.amount * 0.03) + (loan.amount * loan.interest_rate / 365 * 30)
                Billing.objects.create(
                    loan=loan, billing_date=billing_date, due_date=due_date, min_due=min_due
                )
        return Response({'message': 'Billing processed successfully'}, status=status.HTTP_200_OK)

class GetTransactionStatement(APIView):
    def get(self, request):
        loan_id = request.query_params.get('loan_id')
        loan = Loan.objects.filter(id=loan_id).first()
        if not loan:
            return Response({'error': 'Loan does not exist or is closed'}, status=status.HTTP_400_BAD_REQUEST)
        
        past_transactions = []
        payments = loan.payment_set.all()
        for payment in payments:
            past_transactions.append({
                'date': payment.payment_date,
                'principal': loan.amount,
                'interest': loan.amount * loan.interest_rate / 365 * 30,
                'amount_paid': payment.amount
            })

        upcoming_transactions = []
        billings = loan.billing_set.all()
        for billing in billings:
            upcoming_transactions.append({
                'date': billing.due_date,
                'amount_due': billing.min_due
            })

        return Response({
            'past_transactions': past_transactions,
            'upcoming_transactions': upcoming_transactions
        }, status=status.HTTP_200_OK)
