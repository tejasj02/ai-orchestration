import boto3
import json
import time

lambda_client = boto3.client("lambda", region_name="us-east-2")

def invoke_lambda(function_name, payload):
    response = lambda_client.invoke(
        FunctionName=function_name,
        Payload=json.dumps(payload).encode("utf-8"),
    )
    body = response["Payload"].read().decode("utf-8")
    return json.loads(body)

def main():
    prompt = input("Enter your prompt: ").strip()
    if not prompt:
        print("No prompt provided.")
        return

    # Step 1: Validate prompt
    print("→ Calling PromptReceiver...")
    validation_response = invoke_lambda("PromptReceiver", {"prompt": prompt})
    if validation_response.get("statusCode") != 200:
        print("Validation failed:", validation_response)
        return

    # Step 2: Call Groq model (with retries)
    for attempt in range(3):
        print(f"→ Calling CallGroqModel (attempt {attempt + 1})...")
        try:
            model_response = invoke_lambda("CallHFModel", {"prompt": prompt})
            if model_response.get("statusCode") == 200:
                body = json.loads(model_response["body"])
                print("\n✅ Final Response:\n", body["response"])
                return
            else:
                print("Error:", model_response)
        except Exception as e:
            print("Exception:", str(e))
        
        time.sleep(2 ** attempt)  # exponential backoff

    print("Failed after 3 attempts.")

if __name__ == "__main__":
    main()
