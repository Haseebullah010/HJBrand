from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'input100 placeholder0 s2-txt2',
                'placeholder': 'Enter Email Address',
                'name': 'email',
            })
        }
