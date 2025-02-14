from fastapi import APIRouter
from data.customers import create_customers
from models.Customer import Customer_List

customer_router = APIRouter()

@customer_router.get("/customers",
         summary='Get a list of customers with recent life events',
         description='Get a list of customers with recent life events',
         response_description="Customers with recent life events",
         tags=["Customers"]
         )
def customers_with_life_events() -> Customer_List:
    customer_list = create_customers()
    return customer_list

