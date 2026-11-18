import os

import httpx


class PaperSearchError(RuntimeError):
    """A paper search could not be completed."""


def search_papers(topic: str) -> list[dict]:
    """Find up to 10 papers on a topic using OpenAlex.

    Args:
        topic: Search keywords, for example "retrieval augmented generation".
    """
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
        # OpenAlex gives the positions where each word appears in the abstract.
        abstract_index = work.get("abstract_inverted_index") or {}
        positioned_words = [
            (position, word)
            for word, positions in abstract_index.items()
            for position in positions
        ]
        abstract = " ".join(word for _, word in sorted(positioned_words))

        papers.append({
            "title": work["title"],
            "authors": [entry["author"]["display_name"] for entry in work["authorships"]],
            "year": work.get("publication_year"),
            "citation_count": work.get("cited_by_count"),
            "citation_source": "OpenAlex",
            "url": work["id"],
            "abstract": abstract or None,
        })
    return papers
