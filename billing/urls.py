from django.urls import path
from .views import BillingCronJob, GetTransactionStatement

urlpatterns = [
    path('process-billing/', BillingCronJob.as_view(), name='process-billing'),
    path('get-statement/', GetTransactionStatement.as_view(), name='get-statement'),
]
