from django.urls import path, include
from receipts.views import (
    receipt_list,
)

urlpatterns = [
    path("", receipt_list, name="home"),
    ]
