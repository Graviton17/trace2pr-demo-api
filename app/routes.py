from fastapi import APIRouter, HTTPException

from app.services.books import years_since_published
from app.services.orders import order_total, shipping_cost
from app.services.reviews import average_rating
from app.services.search import top_match
from app.services.users import contact_card
from app.store import BOOKS, ORDERS, USERS

router = APIRouter()


def _book(book_id: str):
    if book_id not in BOOKS:
        raise HTTPException(404, "book not found")
    return BOOKS[book_id]


def _order(order_id: str):
    if order_id not in ORDERS:
        raise HTTPException(404, "order not found")
    return ORDERS[order_id]


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/books/{book_id}/rating")
def book_rating(book_id: str):
    _book(book_id)
    return {"book_id": book_id, "average": average_rating(book_id)}


@router.get("/books/{book_id}/age")
def book_age(book_id: str):
    return {"book_id": book_id, "years": years_since_published(_book(book_id))}


@router.get("/orders/{order_id}/total")
def get_order_total(order_id: str):
    return order_total(_order(order_id))


@router.get("/orders/{order_id}/shipping")
def get_shipping(order_id: str):
    return shipping_cost(_order(order_id))


@router.get("/users/{user_id}/contact")
def get_contact(user_id: str):
    if user_id not in USERS:
        raise HTTPException(404, "user not found")
    return contact_card(user_id)


@router.get("/search/top")
def search_top(q: str):
    return top_match(q)
