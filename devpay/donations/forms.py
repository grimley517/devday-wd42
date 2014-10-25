from django import forms
from donations.models import Donations

class DonationForm(forms.ModelForm):
    would_like_newsletter = forms.BooleanField(required=False)
 
    
    class Meta:
        model = Donations
        fields = ('full_name', 'email', 'campaign', 'amount')
        
    
        