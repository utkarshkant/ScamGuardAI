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

### Installation Guides
Refer to this playlist: https://www.youtube.com/playlist?list=PLU6QHAXUQhYlalHlpLyF4DH7WLfPvuXV4

## Project Structure
ScamGuardAI
- experiments
    - `workflow.ipynb`
- llm
    - `__init__.py`
- pipeline
    - `__init__.py`
- streamlit
    - `__init__.py`
- .gitignore
- LICENSE
- README.md
- requirements.txt
- main.py
- utils.py


## Steps Involved in Pipeline
1. Load and configuration setup - DONE
2. LLM Client setup - DONE
3. Prompt template - building the prompt - DONE
4. Handling input - DONE
5. Generate LLM response - DONE
6. Parse output - DONE
7. Showcase output on UI