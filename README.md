# ML_Compulsory2_Research_Assistant
2nd compulsory assignment (research assistant) for machine learning class. 

## Setup
### Step 1: Python virtual environment
On **Windows**, run these commands:  <br />
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On **Mac**: <br />
```
python3 -m venv .venv
source .venv/bin/activate
```


Run some commands to *install packages*: 
```
pip install -r requirements.txt
```


### Step 2: Model setup
We're using models through *Groq's* API. <br />
First, you need to login and setup **API keys** [here](https://console.groq.com/keys) (make sure to copy/paste them somewhere you can access later right after you get the key). You can also access usage data from this site <br />

Then, enter *these commands* to set environment variables: <br />
**Windows:** <br />
```
$env:LLM_BASE_URL="https://api.groq.com/openai/v1"
$env:LLM_MODEL="groq:qwen/qwen3.8-27b"
$env:GROQ_API_KEY="YOUR_API_KEY_HERE"
```
**Mac**: <br />
```
export LLM_BASE_URL="https://api.groq.com/openai/v1"
export LLM_MODEL="groq:qwen/qwen3.8-27b"
export GROQ_API_KEY="YOUR_API_KEY_HERE"
```

You can also put the environment variables in a local `.env` file as `NAME=value` lines.

### Step 3: Run program
run main py file: <br />
```
python main.py
```

Try asking `Find a paper about retrieval-augmented generation. Give its year, citation count, and source.`

`search_papers(topic)` fetches up to 10 OpenAlex matches. The OpenAlex paper page is the source for each citation count. For basic searches, the tool works without a second API key. Set `OPENALEX_API_KEY` for a higher rate limit. [OpenAlex authentication](https://help.openalex.org/api/authentication/)

## Evaluation results

We evaluated 10 prompts covering different topics, publication years, citation limits, and cases where no paper matched. Seven tests were successful and three were partially successful. The agent returned books in two tests and found no match in one test that checked only the first 10 OpenAlex results.

See [evaluation.txt](evaluation.txt) for the prompts, responses, and per-test assessments.

## Group member contributions

- **Jean** implemented the PydanticAI agent.
- **Nelson** implemented the OpenAlex search and filtering tool.
- **Nil** evaluated the agent and documented the results.

We often work together and pair program.
