"""Hit the buggy endpoints so each bug reaches Sentry as its own issue.

    python scripts/trigger_errors.py              # all bugs
    python scripts/trigger_errors.py rating age   # only some
    BASE_URL=http://host:port python scripts/trigger_errors.py
"""

import os
import sys
import urllib.error
import urllib.request

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:8000")

BUGS = {
    "rating": ("/books/b3/rating", "ZeroDivisionError: book with no reviews"),
    "age": ("/books/b4/age", "ValueError: publish date stored as 2019/05/07"),
    "promo": ("/orders/o2/total", "KeyError: unknown promo code SUMMER24"),
    "shipping": ("/orders/o3/shipping", "TypeError: ebook has no weight"),
    "contact": ("/users/u2/contact", "AttributeError: user has no phone"),
    "search": ("/search/top?q=tolkien", "IndexError: search with no matches"),
}


def main(names: list[str]) -> None:
    for name in names or BUGS:
        path, label = BUGS[name]
        try:
            with urllib.request.urlopen(BASE_URL + path) as resp:
                status = resp.status
        except urllib.error.HTTPError as err:
            status = err.code
        print(f"{status}  {name:<9} {path:<24} {label}")


if __name__ == "__main__":
    unknown = [n for n in sys.argv[1:] if n not in BUGS]
    if unknown:
        sys.exit(f"unknown bug(s): {', '.join(unknown)}; choose from {', '.join(BUGS)}")
    main(sys.argv[1:])
