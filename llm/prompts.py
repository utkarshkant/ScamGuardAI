from pathlib import Path
from utils import load_file

PROMPTS_DIR = Path(__file__).parent / "prompt_library"

def load_prompt(filename: str) -> str:
    """
    Load prompt from the prompts directory.
    """
    print(PROMPTS_DIR)
    return load_file(PROMPTS_DIR / filename)

def generate_prompt(user_input: str) -> str:
    """
    Generate a prompt for scam detection
    """
    # template = PROMPT
    template = load_prompt("react.md")
    return f"{template}\n\nUser Message:\n{user_input.strip()}"