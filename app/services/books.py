from datetime import date

from app.store import Book


def years_since_published(book: Book, today: date | None = None) -> int:
    today = today or date.today()
    published = date.fromisoformat(book.published)
    return today.year - published.year
