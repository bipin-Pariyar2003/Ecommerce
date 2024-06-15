from django import forms

class CheckoutForm(forms.Form):
    PAYMENT_CHOICES = (
        ('cod', 'Cash On Delivery'),
        ('online', 'Online Payment'),
    )

    receiver_name = forms.CharField(max_length=200, label='Receiver Name')
    receiver_phone = forms.CharField(max_length=15, label='Receiver Phone')
    receiver_address = forms.CharField(max_length=200, label='Receiver Address')
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
