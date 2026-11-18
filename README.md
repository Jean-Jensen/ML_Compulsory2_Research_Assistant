# ML_Compulsory2_Research_Assistant
2nd compulsory assignment (research assistant) for machine learning class. 

## Setup
### Step 1: Python virtual environment
On **Windows**, run these commands:  <br />
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On **Mac**, do these I guess (idk, I use windows):  <br />
```
python3 -m venv .venv
source .venv/bin/activate
```


Run some commands to *install packages*: 
```
pip install -r requirements.txt
```


### Step 2: Model setup
Right now, we're using *Groq* (not to be confused with Grok). <br />
First, you need to login and setup **API keys** [here](https://console.groq.com/keys) (make sure to copy/paste them somewhere you can access later right after you get the key). You can also access usage data from this site <br />

Then, enter *these commands* to set environment variables: <br />
**Windows:** <br />
```
$env:LLM_BASE_URL="https://api.groq.com/openai/v1"
$env:LLM_MODEL="groq:qwen/qwen3.8-27b"
$env:GROQ_API_KEY="YOUR_API_KEY_HERE"
```
**Mac**: (once again, untested) <br />
```
export LLM_BASE_URL="https://api.groq.com/openai/v1"
export LLM_MODEL="groq:qwen/qwen3.8-27b"
export GROQ_API_KEY="YOUR_API_KEY_HERE"
```

You can also put the settings in a local `.env` file as `NAME=value` lines.

### Step 3: Run program
run main py file: <br />
```
python main.py
```

Try asking `Find a paper about retrieval-augmented generation. Give its year, citation count, and source.`

`search_papers(topic)` fetches up to 10 OpenAlex matches. The OpenAlex paper page is the source for each citation count. For basic searches, the tool works without a second API key. Set `OPENALEX_API_KEY` for a higher rate limit. [OpenAlex authentication](https://help.openalex.org/api/authentication/)
