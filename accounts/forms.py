from django import forms
from django.contrib.auth.models import User

class UserSearchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)

    def search_users(self):
        username = self.cleaned_data['username']
        return User.objects.filter(username__icontains=username)

TRANSACTION_CHOICES = [
    ('deposit', 'Deposit'),
    ('credit', 'Credit'),
]

class TransactionForm(forms.Form):
    transaction_type = forms.ChoiceField(choices=TRANSACTION_CHOICES)
    amount = forms.FloatField()