from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import stripe

payment_router = APIRouter()

# Настройте ваш секретный ключ Stripe
stripe.api_key = "sk_test_51Q1vKG2LHVjB2yaT35oEHz8c0mqunbPFnbj7MxCUvehC5PQSGJmqSBf3MoSmUH8vQqR7UKuzZxUGWs8Og19Qt9iW00I8oapMuE"


class PaymentRequest(BaseModel):
    amount: int
    currency: str
    payment_method_id: str


@payment_router.post("/create-payment")
async def create_payment(payment: PaymentRequest):
    try:
        intent = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency=payment.currency,
            payment_method=payment.payment_method_id,
            confirm=True,
        )
        return {"success": True, "payment_intent": intent.id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@payment_router.get("/payment-status/{payment_intent_id}")
async def payment_status(payment_intent_id: str):
    try:
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return {"status": intent.status}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))