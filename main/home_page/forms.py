from django import forms
from .models import Newsletter, Fillup


class FillForm(forms.ModelForm):
    class Meta:
        model = Fillup
        fields = ['Name', 'Email', 'Service', 'Message']
        
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['Email']