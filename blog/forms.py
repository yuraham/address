from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('name', 'numb', 'numb_num', 'email',)