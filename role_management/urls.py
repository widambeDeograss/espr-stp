from django.urls import path
from .views import *

app_name = 'role_management'

urlpatterns = [
    path('role', RolesView.as_view()),
]
