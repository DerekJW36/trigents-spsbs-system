import stripe
import os
import logging

logger = logging.getLogger(__name__)

# To use this, the user must set STRIPE_SECRET_KEY in their .env
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_placeholder")

class PaymentManager:
    @staticmethod
    def create_payment_link(amount: int, currency: str = "usd", description: str = "Auto Part Order") -> str:
        """
        Creates a Stripe payment link for the given amount (in cents).
        Returns the URL to the payment link.
        """
        try:
            # Create a product and price on the fly for the demo
            product = stripe.Product.create(name=description)
            price = stripe.Price.create(
                unit_amount=amount,
                currency=currency,
                product=product.id,
            )
            
            # Create the payment link
            payment_link = stripe.PaymentLink.create(
                line_items=[{"price": price.id, "quantity": 1}]
            )
            logger.info(f"Created Stripe Payment Link: {payment_link.url}")
            return payment_link.url
            
        except Exception as e:
            logger.error(f"Failed to create Stripe payment link: {e}")
            # Mock URL for demo purposes if Stripe is not configured yet
            return "https://buy.stripe.com/test_mock_link123"

# Expose a function that the AI tool can call
def generate_payment_link_tool(part_name: str, price_dollars: float, customer_phone: str) -> dict:
    """
    Called by the AI to generate a payment link and 'send' it to the customer.
    In a real app, this would use Twilio to SMS the link to `customer_phone`.
    """
    amount_in_cents = int(price_dollars * 100)
    link = PaymentManager.create_payment_link(amount_in_cents, description=part_name)
    
    # Mock SMS Sending
    logger.info(f"Mock SMS Sent to {customer_phone}: 'Complete your order for {part_name} here: {link}'")
    
    return {
        "status": "success",
        "message": f"Payment link generated and sent via SMS to {customer_phone}",
        "url": link
    }
