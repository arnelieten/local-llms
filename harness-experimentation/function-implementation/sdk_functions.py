"""SDK-backed functions for harness evaluation.

Implement each function body. Do not change signatures or docstrings.
Credentials / API keys are provided at call time by the experimenter.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd


def summarize_text(text: str, api_key: str) -> str:
    """Summarize ``text`` using the OpenAI Chat Completions API.

    Use the official ``openai`` Python client. Prefer a small, cheap model
    such as ``gpt-4o-mini``. Return only the assistant's summary string
    (no JSON wrapper).

    Args:
        text: Source text to summarize. Must be non-empty.
        api_key: OpenAI API key (do not hard-code; use the argument).

    Returns:
        A short natural-language summary of ``text``.

    Raises:
        ValueError: If ``text`` is empty or whitespace-only.
        Exception: Propagates client / API errors.

    Notes:
        Requires network access and a valid ``api_key``.
    """
    raise NotImplementedError


def top_customers_by_revenue(csv_path: str, n: int) -> "pd.DataFrame":
    """Return the top ``n`` customers by total revenue from a CSV file.

    The CSV must contain at least the columns ``customer`` and ``revenue``.
    Group by ``customer``, sum ``revenue``, sort descending by the sum,
    and return the first ``n`` rows as a DataFrame with columns
    ``customer`` and ``revenue`` (the summed revenue).

    Args:
        csv_path: Path to the CSV file.
        n: Number of top customers to return. Must be >= 1.

    Returns:
        A pandas DataFrame with columns ``customer``, ``revenue``,
        sorted by ``revenue`` descending, length ``min(n, unique customers)``.

    Raises:
        ValueError: If ``n`` < 1 or required columns are missing.
        FileNotFoundError: If ``csv_path`` does not exist.

    Notes:
        Uses the ``pandas`` library.
    """
    raise NotImplementedError


def upload_file_to_gcs(local_path: str, bucket_name: str, dest_blob: str) -> str:
    """Upload a local file to a Google Cloud Storage bucket.

    Use ``google.cloud.storage.Client`` (Application Default Credentials
    or the environment the experimenter has configured). Upload
    ``local_path`` to ``gs://{bucket_name}/{dest_blob}``.

    Args:
        local_path: Path to an existing local file.
        bucket_name: Target GCS bucket name.
        dest_blob: Destination object name (path inside the bucket).

    Returns:
        The GCS URI of the uploaded object, e.g.
        ``gs://my-bucket/path/to/file.txt``.

    Raises:
        FileNotFoundError: If ``local_path`` does not exist.
        Exception: Propagates GCS client errors.

    Notes:
        Requires ``google-cloud-storage`` and valid GCP credentials.
    """
    raise NotImplementedError
