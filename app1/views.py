from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            stripe.Charge.create(
            amount=200000,
            currency="inr",
            source="tok_visa",
            description="My First Test Charge (created for API docs)",
            )
        except stripe.error.CardError as e:
            print(e)
    return render(request, 'checkout.html', {'publishKey': publishKey})
