def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_book_rating(client):
    assert client.get("/books/b1/rating").json() == {"book_id": "b1", "average": 4.67}


def test_unknown_book_404(client):
    assert client.get("/books/nope/rating").status_code == 404


def test_book_age(client):
    assert client.get("/books/b1/age").json()["years"] >= 60


def test_order_total_with_promo(client):
    data = client.get("/orders/o1/total").json()
    assert data["subtotal_cents"] == 4897
    assert data["discount_cents"] == 489
    assert data["total_cents"] == 4408


def test_order_total_without_promo(client):
    data = client.get("/orders/o4/total").json()
    assert data["discount_cents"] == 0
    assert data["total_cents"] == 3798


def test_shipping(client):
    data = client.get("/orders/o4/shipping").json()
    assert data["weight_kg"] == 1.8
    assert data["shipping_cents"] == 299 + 270


def test_contact_card(client):
    data = client.get("/users/u1/contact").json()
    assert data["phone"] == "+442079460018"


def test_search_top(client):
    data = client.get("/search/top", params={"q": "gibson"}).json()
    assert data["top"]["id"] == "b2"
    assert data["total"] == 1
