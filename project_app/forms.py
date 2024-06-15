from django import forms

class CheckoutForm(forms.Form):
    receiver_name = forms.CharField(max_length=200, label='Receiver Name')
    receiver_phone = forms.CharField(max_length=15, label='Receiver Phone')
    receiver_address = forms.CharField(max_length=200, label='Receiver Address')
