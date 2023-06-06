from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()

# Payment Model
class Payment(BaseModel):
    credit_card_number: str
    expiry_date: str
    cvv_number: int
    payment_amount: float

# Payment Service
@app.post("/payment")
def payment_service(payment: Payment):
    # code to handle payment
    payment_response = {
        "status": "success",
        "transaction_id": "1234567890"
    }
    return payment_response

# Payment Success Redirect
@app.get("/payment/success")
def payment_success(request: Request, response: Response):
    # code to redirect the user to successful payment page
    response.status_code = 302
    response.headers["Location"] = "https://example.com/payment/success"
    return response

# Payment Failure Redirect
@app.get("/payment/failure")
def payment_failure(request: Request, response: Response):
    # code to redirect the user to failed payment page
    response.status_code = 302
    response.headers["Location"] = "https://example.com/payment/failure"
    return response

# Logging Payment Errors
@app.exception_handler(Exception)
def payment_exception_handler(request: Request, exc: Exception):
    # code to log payment related errors
    print(f"Error: {exc}")