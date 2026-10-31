from app.store import BOOKS, PROMOS, Order

SHIPPING_BASE_CENTS = 299
SHIPPING_PER_KG_CENTS = 150


def subtotal_cents(order: Order) -> int:
    return sum(BOOKS[line.book_id].price_cents * line.quantity for line in order.lines)


def order_total(order: Order) -> dict:
    subtotal = subtotal_cents(order)
    discount = 0
    if order.promo_code:
        discount = int(subtotal * PROMOS[order.promo_code])
    return {
        "order_id": order.id,
        "subtotal_cents": subtotal,
        "discount_cents": discount,
        "total_cents": subtotal - discount,
    }


def shipping_cost(order: Order) -> dict:
    weight = sum(BOOKS[line.book_id].weight_kg * line.quantity for line in order.lines)
    cost = SHIPPING_BASE_CENTS + int(weight * SHIPPING_PER_KG_CENTS)
    return {"order_id": order.id, "weight_kg": round(weight, 2), "shipping_cents": cost}
