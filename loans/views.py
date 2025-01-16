from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan
from .serializers import LoanSerializer
from users.models import User

class ApplyLoanView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.filter(id=user_id).first()
        if not user or user.credit_score < 450:
            return Response({'error': 'User not eligible for loan'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
