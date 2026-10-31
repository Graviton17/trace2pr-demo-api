"""Demo bookstore API instrumented with Sentry for the Trace2PR pipeline."""

import os
import subprocess

import sentry_sdk
from fastapi import FastAPI

from app.routes import router


def git_sha() -> str:
    if sha := os.environ.get("GIT_SHA"):
        return sha
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "dev"


def init_sentry() -> None:
    dsn = os.environ.get("SENTRY_DSN")
    if not dsn:
        return
    # Trace2PR maps errors to the deployed commit through the release.
    sentry_sdk.init(
        dsn=dsn,
        release=f"trace2pr-demo-api@{git_sha()}",
        environment=os.environ.get("APP_ENV", "development"),
        traces_sample_rate=0.0,
    )


def create_app() -> FastAPI:
    init_sentry()
    app = FastAPI(title="Bookstore API")
    app.include_router(router)
    return app


app = create_app()
