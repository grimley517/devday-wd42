import braintree
from django.conf import settings

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    merchant_id = settings.BT_MERCH_ID,
    public_key = settings.BT_PUBKEY,
    private_key = settings.BT_PRIVATE_KEY
)

def getClientID():
    return braintree.ClientToken.generate()

def do_payment(ammount,nonce):
    result = braintree.Transaction.sale({
        "amount": ammount,
        "payment_method_nonce": "nonce-from-the-client"
    })
    return result