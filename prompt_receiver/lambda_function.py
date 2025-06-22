import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    prompt = event.get("prompt", "").strip()
    
    if not prompt:
        logger.warning("No valid prompt provided.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Prompt is required."})
        }
    
    logger.info(f"Received prompt: {prompt}")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Prompt received.", "prompt": prompt})
    }
