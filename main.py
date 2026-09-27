"""
Main application runner.
"""

from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from utils import get_logger

# path normalization
project_root = Path(__file__).parent
sys.path.append(str(project_root))
logger = get_logger(__name__)

# main runner function - calls scam detection workflow
def main():
    """
    Main function for running the Scam Detection pipeline.
    """

    detector = ScamDetector()
    # test_message = "You have an unclaimed policy for $10000, fill the details to claim it, otherwise it will expire in the next 2 hours."
    test_message = input("Enter your message to detect scam: ")

    try:
        logger.info("Running the scam detection workflow.")
        result = detector.detect(test_message)
        print(f"Input message: {test_message}")
        print(f"Detection result: {result}")
        logger.info("Scam detection completed successfully.")

    except Exception as e:
        logger.error(f"Error occurred during scam detection: {e}")
        print(f"Error occurred during scam detection: {e}")

if __name__ == "__main__":
    main()