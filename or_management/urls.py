from django.urls import path
from .views import *

app_name = 'order_management'

urlpatterns = [
    path('order', OrderView.as_view()),
    path('income-transaction', IncomeTransactionView.as_view()),
    path('client', ClientView.as_view()),
    path('order-status/<slug:order_id>/<int:new_status>', ClientView.as_view()),
]
