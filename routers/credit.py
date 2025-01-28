from fastapi import APIRouter

from models.Credit import CreditRequest, CreditResponse

credit_router = APIRouter()


def credit_calc(credit:float, rate:float):
    n =  12  # total number of months
    r = rate / (100 * 12)  # interest per month
    monthly_payment = credit * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
    return monthly_payment
@credit_router.post("/credit")
def credit(credit_request: CreditRequest)->CreditResponse:

    monthlyPayment = credit_calc(credit_request.credit, credit_request.rate)
    totalPayment = monthlyPayment * 12

    cr = CreditResponse(monthly=round(monthlyPayment,2), total=round(totalPayment,2))

    return cr

