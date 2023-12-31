from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm
# Create your views here.


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            #Creates an object but doesn't save
            receipt = form.save(False)
            receipt.purchaser = request.user
            #saves here
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            return redirect("categories_list")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
    }
    return render(request, "categories/create.html", context)

@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("accounts_list")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/create.html", context)



@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def categories_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "categories/list.html", context)


@login_required
def accounts_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "accounts/list.html", context)
