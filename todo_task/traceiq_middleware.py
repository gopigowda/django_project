import traceback
import threading
import urllib.request
import urllib.error
import json
import logging

logger = logging.getLogger(__name__)

TRACEIQ_INGEST_URL = "http://localhost:8000/api/ingest"
TRACEIQ_INGEST_SECRET = "NidzH5JXLxgsBRwfaSyzARUjsTcd9vUvDfDvVxDreu8"
TRACEIQ_ORG_ID = "ec04190e-5c01-4cc5-97bd-52026225943e"
TRACEIQ_REPO_ID = "265ee11c-bc87-4523-bb83-713bdbe9e6cc"
TRACEIQ_SERVICE_NAME = "django_project"


def _send_to_traceiq(error_message: str, stack_trace: str, log_level: str = "ERROR") -> None:
    payload = json.dumps({
        "organization_id": TRACEIQ_ORG_ID,
        "repository_id": TRACEIQ_REPO_ID,
        "log_level": log_level,
        "error_message": error_message,
        "stack_trace": stack_trace,
        "service_name": TRACEIQ_SERVICE_NAME,
    }).encode("utf-8")

    req = urllib.request.Request(
        TRACEIQ_INGEST_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Ingest-Secret": TRACEIQ_INGEST_SECRET,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            logger.info("TraceIQ ingest accepted: %s", resp.read().decode())
    except Exception as exc:
        logger.warning("TraceIQ ingest failed: %s", exc)


class TraceIQMiddleware:
    """
    Sends an incident to TraceIQ only when a view raises an unhandled exception.
    Normal page loads (200, 404, etc.) never trigger ingest.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        # process_exception is called ONLY when a view raises an exception.
        # It is never called on normal responses.
        error_message = f"{type(exception).__name__}: {exception}"
        stack_trace = traceback.format_exc()

        # Fire-and-forget in background thread so the error response isn't delayed.
        threading.Thread(
            target=_send_to_traceiq,
            args=(error_message, stack_trace),
            daemon=True,
        ).start()

        # Return None so Django continues with its normal exception handling
        # (shows the 500 page / DEBUG traceback as usual).
        return None
