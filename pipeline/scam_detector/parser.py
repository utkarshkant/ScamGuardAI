from typing import Dict, Any
from utils import get_logger, extract_json_from_text

logger = get_logger(__name__)

class OutputParser:
    """
    Class for handing and parsing LLM output.
    """

    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        """
        Extracts and Parse JSON structure from the LLM output.

        Args:
            llm_output: Raw string output from the LLM.
        
        Returns:
            Dictionary that contains results from the LLM output.
            - label: str -> Classification result (Scam / No Scam / Uncertain),
            - reasoning: str -> Analysis of the classification,
            - intent: str -> Intent of the message sender,
            - risk_factors: List[str] -> List of identified red flags in the message 
        """
        logger.info("Begin output parsing.")

        parsed_json = extract_json_from_text(llm_output)

        if parsed_json:
            logger.info("Successfully parsed the LLM output to JSON.")
            return parsed_json

        else:
            logger.warning("No JSON found in the LLM output")
            fallback_results = {
                "label": "Uncertain", 
                "reasoning": "Could not parse AI response",
                "intent": "Unknown",
                "risk_factors": ["Parsing Error"]
                }
            return fallback_results