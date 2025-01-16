from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from loans.models import Loan

class MakePaymentView(APIView):
    def post(self, request):
        loan_id = request.data.get('loan_id')
        amount = request.data.get('amount')

        loan = Loan.objects.filter(id=loan_id).first()
        if not loan:
            return Response({'error': 'Invalid loan ID'}, status=status.HTTP_400_BAD_REQUEST)

        if amount < loan.amount * 0.03:
            return Response({'error': 'Amount less than minimum due'}, status=status.HTTP_400_BAD_REQUEST)

        Payment.objects.create(loan=loan, amount=amount, payment_date=date.today())
        return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
