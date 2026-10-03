from typing import List, Dict, Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

logger = get_logger(__name__)

class ScamDetector:
    """
    The main class for detecting scam in user messages.
    """

    def __init__(self, strategy: str = "react") -> None:
        """
        Initialized the scam detection pipeline
        """
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialized ScamDetector with Strategy -> {self.strategy}")
        

    def detect(self, message: str) -> Dict[str, Any]:
        """
        Runs the main scam detection pipeline.
        """
        logger.info(f"Started the scam detection for input message")
        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)

            logger.info(f"Detection is successful!")
            return parsed_result

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")