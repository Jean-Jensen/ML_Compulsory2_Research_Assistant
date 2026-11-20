## Reflection

### What worked well?

Most of the test prompts worked pretty well. The agent was able to understand what kind of paper we were looking for, including the topic, publication year and citation requirements. It could then search OpenAlex and return a paper that matched the requirements.

The year and citation filters also worked as expected in our tests. I think it was good that the citation counts came directly from OpenAlex instead of letting the LLM make them up.

### What failed or was unreliable?

There were a few things that did not work as well.

In Test 1 and Test 4, the agent returned a book or textbook instead of a research paper. This is because our search tool does not check the publication type.

In Test 7, the agent could not find a paper that matched the requirements. However, our tool only searches through the first 10 results, so there might actually be a suitable paper further down the list.

We also had some problems with the OpenAlex API during Test 10, including rate limits and server errors. We tried again later, and the request eventually worked.

### How often did the agent need tool calls?

We told the agent to call `search_papers` every time the user asks for a paper. In most cases, one search call was enough to get the results.

We did not keep track of the exact number of tool calls, so we cannot say exactly how many were made. Test 10 also needed a retry because of the API errors.

### Did the LLM ever hallucinate?

We did not notice any clear cases where the LLM made up paper titles, authors or citation counts in our tests.

However, in Test 1 and Test 4, it returned books instead of research papers. This shows that it does not always understand the difference between the two.

In some tests, such as Test 3 and Test 6, the agent also gave quite detailed explanations with extra information about the papers. We did not check every detail separately, so we cannot say for sure whether all of this information was correct. This is something to keep in mind when using the agent.

### How did you prevent incorrect answers?

We tried to reduce the chance of incorrect answers in a few ways:

- Citation counts come from OpenAlex, not from the LLM.
- Python checks the publication year and citation requirements.
- The agent is told to use the information returned by the search tool.
- It is also told not to return a paper if it does not match the user's requirements.
- If no matching paper is found, it should say so instead of choosing a paper that does not fit.

These checks help, but they do not guarantee that every answer will be correct.

### What would you improve with more time?

If we had more time, we would improve the search so that it could filter out books and other types of publications that are not research papers. We would also increase the number of search results from 10, since we might miss relevant papers otherwise.

It would also be useful to check the agent's final answer against the original information from OpenAlex to make sure that it has not changed any details.

Lastly, we could keep better track of tool calls and API errors during testing. That would make it easier to evaluate how the agent actually performs.