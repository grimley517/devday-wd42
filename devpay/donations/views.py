from django.shortcuts import render
from donations.payment import getClientID, do_payment
from donations.models import Donations, Campaign
from donations.forms import DonationForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            nonce = request.POST['payment_method_nonce']
            payment_result = do_payment(amount,nonce)
            form.save()
            return render(request, 'success.html', {'result':payment_result,
                'amount':payment_result,
                })
    else:
        form = DonationForm()
        
    donations = Donations.objects.order_by('-amount')
    campaign = Campaign.objects.all()
    return render(request,"donate.html" ,{
            'BT_CLIENT_KEY':getClientID(),
            'donations':donations,
            'campaigns':campaign,
            'form':form,
        })

