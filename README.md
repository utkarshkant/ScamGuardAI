# ScamGuardAI

LLM powered application to detect Scam messages.

## Commands to be followed

### git commands
```
git clone https://github.com/utkarshkant/ScamGuardAI.git
git status
git add . / git add <file_name>
git commit -m "message"
git push origin main
git pull
```

### Environment management
```
conda create -n <env_name> python=3.11 -y
conda activate <env_name>
conda deactivate
pip install -r requirements.txt
```

### For creating venv using Python
```
winget install Python.Python.3.11
After installation, close and reopen PowerShell, then verify:
py -3.11 --version
You should see something like:
Python 3.11.9
Then create your environment:
py -3.11 -m venv scamgaurd
Activate:
.\scamgaurd\Scripts\Activate.ps1
```
### Setup the Environment variables
- Update the `.env-template` file to `.env` file
- Add your `GEMINI_API_KEY`

### Run the app
Activate the virtual environment, then the run the app with the following command.
```
python main.py
```

To run the UI, activate the virtual environment, and run the below command.
```
streamlit run streamlit\app.py
```

### Installation Guides
Refer to this playlist: https://www.youtube.com/playlist?list=PLU6QHAXUQhYlalHlpLyF4DH7WLfPvuXV4

## Project Structure

```text
ScamGuardAI/
├── .env
├── .env-template
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── __init__.py
├── config.py
├── main.py
├── utils.py
├── experiments/
│   └── workflow.ipynb
├── llm/
│   ├── __init__.py
│   ├── client.py
│   ├── prompts.py
│   └── prompt_library/
│       ├── __init__.py
│       └── react.md
├── pipeline/
│   ├── __init__.py
│   └── scam_detector/
│       ├── __init__.py
│       ├── builder.py
│       ├── detector.py
│       ├── executor.py
│       └── parser.py
└── streamlit/
    ├── __init__.py
    └── app.py
```
