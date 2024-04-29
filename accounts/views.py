from django.shortcuts import render
from .forms import UserSearchForm, TransactionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserAccount


def search_users(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            users = form.search_users()
            return render(request, 'search_results.html', {'users': users})
    else:
        form = UserSearchForm()
    return render(request, 'search_users.html', {'form': form})


@login_required
def account_info(request):
    user_account = UserAccount.objects.get(user=request.user)
    return render(request, 'account_info.html', {'user_account': user_account})

@login_required
def make_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction_type = form.cleaned_data['transaction_type']
            user_account = UserAccount.objects.get(user=request.user)
            if transaction_type == 'deposit':
                user_account.balance += amount
            elif transaction_type == 'credit':
                user_account.points += amount
            user_account.save()
            return redirect('account_info')
    else:
        form = TransactionForm()
    return render(request, 'make_transaction.html', {'form': form})
