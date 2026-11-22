# Agent Workflow

1. **Python** reads the user's request from the terminal and passes it to the PydanticAI agent.
2. **LLM** identifies the topic, publication year and citation count. The agent is instructed to call `search_papers` for every paper request and pass those values as tool arguments.
3. **Python** searches OpenAlex by topic and retrieves up to 10 results. It then applies the year condition and inclusive citation limits. If a result is missing a value needed for a filter, Python skips it. The tool returns the remaining records with their metadata and abstracts when available.
4. **LLM** uses the returned records to choose one relevant paper and explain why it matches. The answer includes the title, authors, year, citation count from OpenAlex, and the OpenAlex link. The agent is instructed to report when no returned paper qualifies or when the selected paper's citation count is unavailable.
5. **Python** prints the answer. If the search fails, the terminal shows the search error.

The filters only check the first 10 results per search and can leave out matches farther down. 
