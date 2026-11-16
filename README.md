# ML_Compulsory2_Research_Assistant
2nd compulsory assignment (research assistant) for machine learning class. 

## Setup
### Step 1: Python virtual environment
on windows, run these commands:  <br />
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
<br />
on mac, do these I guess (idk, I use windows):  <br />
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manual_room.py --demo
python -m unittest -v test_previous
```
<br />

Run some commands to install packages:
```
pip install pydantic-ai  
pip install "pydantic-ai-slim[groq]"
```


### Step 2: Model setup
Right now, we're using Groq (not to be confused with Grok). <br />
First, you need to login and setup API keys [here](https://console.groq.com/keys) (make sure to copy/paste them somewhere you can access later)  <br />

Then, enter these commands to set environment variables: <br />
Windows: <br />
```
$env:LLM_BASE_URL="https://api.groq.com/openai/v1"
$env:LLM_MODEL="groq:qwen/qwen3.8-27b"
$env:GROQ_API_KEY="YOUR_API_KEY_HERE"
```
Mac: (once again, untested) <br />
```
export LLM_BASE_URL="https://api.groq.com/openai/v1"
export LLM_MODEL="groq:qwen/qwen3.8-27b"
export GROQ_API_KEY="YOUR_API_KEY_HERE"
```

