
import os
import httpx
from typing import Literal  # restrict the year operator to specific values (we learnin week 44)


class PaperSearchError(RuntimeError):
    """A paper search could not be completed."""


def search_papers(
    topic: str,
    year: int | None = None,
    year_operator: Literal["before", "after", "exact"] | None = None,
    min_citations: int | None = None,
    max_citations: int | None = None,
) -> list[dict]:
    """Find papers on a topic using OpenAlex and optionally filter them."""

    api_key = os.getenv("OPENALEX_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    try:
        response = httpx.get(
            "https://api.openalex.org/works",
            params={
                "search": topic,
                "per_page": 10,
                "select": "id,title,authorships,publication_year,cited_by_count,abstract_inverted_index",
            },
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()

    except httpx.HTTPStatusError as error:
        status = error.response.status_code
        if status == 429:
            raise PaperSearchError("OpenAlex rate limit reached. Try again later.") from error
        raise PaperSearchError(f"OpenAlex returned HTTP {status}.") from error

    except httpx.RequestError as error:
        raise PaperSearchError("Could not reach OpenAlex.") from error

    except ValueError as error:
        raise PaperSearchError("OpenAlex returned invalid JSON.") from error

    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise PaperSearchError("OpenAlex returned an unexpected search response.")

    papers = []

    for work in payload["results"]:

        # Safely get the paper information.
        # This avoids errors if some fields are missing from OpenAlex.
        title = work.get("title")
        authorships = work.get("authorships") or []
        publication_year = work.get("publication_year")
        citation_count = work.get("cited_by_count")

        if year is not None and year_operator is not None:

            # If the publication year is missing, we cannot verify the requirement.
            if publication_year is None:
                continue

            if year_operator == "before" and publication_year >= year:
                continue

            elif year_operator == "after" and publication_year <= year:
                continue

            elif year_operator == "exact" and publication_year != year:
                continue

        #
        if min_citations is not None:
            if citation_count is None or citation_count < min_citations:
                continue

        if max_citations is not None:
            if citation_count is None or citation_count > max_citations:
                continue

        # OpenAlex gives the positions where each word appears in the abstract.
        abstract_index = work.get("abstract_inverted_index") or {}

        positioned_words = [
            (position, word)
            for word, positions in abstract_index.items()
            for position in positions
        ]

        abstract = " ".join(
            word for _, word in sorted(positioned_words)
        )

        papers.append({
            "title": title,
            "authors": [
                entry["author"]["display_name"]
                for entry in authorships
                if entry.get("author") and entry["author"].get("display_name")
            ],
            "year": publication_year,
            "citation_count": citation_count,
            "citation_source": "OpenAlex",
            "url": work.get("id"),
            "abstract": abstract or None,
        })

    return papers
