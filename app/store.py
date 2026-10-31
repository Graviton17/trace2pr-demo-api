"""In-memory data standing in for a database."""

from dataclasses import dataclass, field


@dataclass
class Book:
    id: str
    title: str
    author: str
    price_cents: int
    published: str
    weight_kg: float | None  # None for ebooks


@dataclass
class OrderLine:
    book_id: str
    quantity: int


@dataclass
class Order:
    id: str
    user_id: str
    lines: list[OrderLine] = field(default_factory=list)
    promo_code: str | None = None


BOOKS = {
    "b1": Book("b1", "Dune", "Frank Herbert", 1899, "1965-08-01", 0.9),
    "b2": Book("b2", "Neuromancer", "William Gibson", 1499, "1984-07-01", 0.4),
    "b3": Book("b3", "The Dispossessed", "Ursula K. Le Guin", 1650, "1974-05-01", 0.5),
    "b4": Book("b4", "Exhalation", "Ted Chiang", 1299, "2019/05/07", 0.6),
    "b5": Book("b5", "Snow Crash (ebook)", "Neal Stephenson", 999, "1992-06-01", None),
}

REVIEWS = {
    "b1": [5, 4, 5],
    "b2": [4, 3],
    "b4": [5],
}

USERS = {
    "u1": {"id": "u1", "name": "Ada Lovelace", "email": "ada@example.com", "phone": "+44 20 7946 0018"},
    "u2": {"id": "u2", "name": "Alan Turing", "email": "alan@example.com", "phone": None},
}

PROMOS = {"WELCOME10": 0.10, "BOOKWORM": 0.15}

ORDERS = {
    "o1": Order("o1", "u1", [OrderLine("b1", 1), OrderLine("b2", 2)], "WELCOME10"),
    "o2": Order("o2", "u2", [OrderLine("b3", 1)], "SUMMER24"),
    "o3": Order("o3", "u1", [OrderLine("b2", 1), OrderLine("b5", 1)]),
    "o4": Order("o4", "u2", [OrderLine("b1", 2)]),
}
