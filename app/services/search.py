from app.store import BOOKS


def search_books(query: str) -> list[dict]:
    q = query.lower()
    return [
        {"id": b.id, "title": b.title, "author": b.author}
        for b in BOOKS.values()
        if q in b.title.lower() or q in b.author.lower()
    ]


def top_match(query: str) -> dict:
    matches = search_books(query)
    return {"query": query, "top": matches[0], "total": len(matches)}
