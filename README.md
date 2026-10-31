# trace2pr-demo-api

A small FastAPI bookstore API with six planted backend bugs, used to test
[Trace2PR](https://github.com/) end to end: error → Sentry → Trace2PR → draft PR.

The test suite only covers the happy paths, so it passes. Each bug raises an
unhandled exception that Sentry reports as its own issue.

| Trigger | Request | Exception | File |
|---|---|---|---|
| `rating` | `GET /books/b3/rating` | `ZeroDivisionError` | `app/services/reviews.py` |
| `age` | `GET /books/b4/age` | `ValueError` | `app/services/books.py` |
| `promo` | `GET /orders/o2/total` | `KeyError` | `app/services/orders.py` |
| `shipping` | `GET /orders/o3/shipping` | `TypeError` | `app/services/orders.py` |
| `contact` | `GET /users/u2/contact` | `AttributeError` | `app/services/users.py` |
| `search` | `GET /search/top?q=tolkien` | `IndexError` | `app/services/search.py` |

## Run

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest
SENTRY_DSN=... uvicorn app.main:app --port 8000
```

The Sentry release is `trace2pr-demo-api@<git sha>` (from `GIT_SHA`, or
`git rev-parse HEAD`), so Trace2PR checks out the exact deployed commit.
Push your commits before triggering errors, so that commit exists on GitHub.

In another terminal:

```bash
python scripts/trigger_errors.py            # all six bugs
python scripts/trigger_errors.py rating     # just one
```

## Trace2PR flow

1. Push this repo to GitHub.
2. In Sentry, create a Python project and copy its DSN.
3. In Trace2PR, connect GitHub and Sentry, map the Sentry project to this repo,
   and paste the Trace2PR webhook URL into Sentry (internal integration with
   the `issue` and `error` webhooks, or an alert rule's webhook action).
4. Run the app with `SENTRY_DSN` and trigger a bug.
5. In Trace2PR, open the incident, click **Generate fix**, and review the draft PR.
   The PR should fix the bug and add a test that fails before the fix.

To reset after merging fixes, revert the merge commits or re-plant a bug.
