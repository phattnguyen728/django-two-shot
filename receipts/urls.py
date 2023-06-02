from django.urls import path, include
from receipts.views import (
    receipt_list,
    create_receipt,
    categories_list,
    accounts_list,
    create_category,
    create_account,
)

urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", categories_list, name="categories_list"),
    path("accounts/", accounts_list, name="accounts_list"),
    path("categories/create/", create_category, name="create_category"),
    path("accounts/create/", create_account, name="create_account"),
    ]
