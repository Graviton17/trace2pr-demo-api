from app.store import REVIEWS


def average_rating(book_id: str) -> float:
    ratings = REVIEWS.get(book_id, [])
    return round(sum(ratings) / len(ratings), 2)
