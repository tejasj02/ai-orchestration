# AI Orchestration Pipeline

## Overview

This project implements a simple AI pipeline using AWS Lambda and the Groq API. It validates a user prompt, sends it to a hosted language model, and returns a response. The system includes basic monitoring, logging, and retry mechanisms.

---

## Architecture

```plaintext
User Input
    ↓
orchestrator.py
    ↓
PromptReceiver (Lambda) ──→ validates prompt
    ↓
CallGroqModel (Lambda) ──→ calls Groq LLaMA 3 model
    ↓
Returns final response
```

## Components

PromptReceiver – validates input (non-empty prompt)

CallGroqModel – calls Groq's hosted llama3-8b-8192 via REST

orchestrator.py – runs locally, invokes both functions with retry logic

CloudWatch – tracks logs, errors, and usage

## How to Run

Make sure AWS CLI is configured

Set GROQ_API_KEY as an environment variable in Lambda

Set virtual environment with pip install requirements.txt

Run: python orchestrator.py

## Monitoring

CloudWatch dashboard includes Invocation and Error counts
![image](https://github.com/user-attachments/assets/95b9772c-a832-482b-85c1-ebf53180c5d0)

Logs available in /aws/lambda/<function_name>

## Notes
Retry logic is handled locally (up to 3 attempts)

All components run serverlessly using AWS free tier
