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

## Example Working Orchestration of Implementation
```
(venv) PS C:\Users\thete\Github\ai-orchestration> python orchestrator.py
Enter your prompt: how to eat cake
→ Calling PromptReceiver...
→ Calling CallGroqModel (attempt 1)...

✅ Final Response:
 Eating cake is a delightful experience! Here's a step-by-step guide on how to enjoy your delicious cake:

1. **Prepare your cake**: Make sure your cake is at room temperature. If it's been refrigerated or frozen, let it thaw and come to room temperature before serving.
2. **Choose your serving method**: You can serve cake in slices, squares, or even cubes, depending on the type of cake and the occasion. For a more formal presentation, consider slicing the cake into thin, uniform pieces.
3. **Hold the cake**: Hold the cake slice or piece in your dominant hand, with the flat side facing up. If you're serving a cupcake, you can hold it in your hand or place it on a plate.
4. **Take a bite**: Bring the cake to your mouth and take a small to moderate-sized bite. Try to take a bite that includes a mix of cake, frosting, and any toppings or fillings.
5. **Chew and savor**: Chew your cake slowly and mindfully, paying attention to the texture, flavor, and aroma. Let the sweetness and flavors meld together in your mouth.
6. **Enjoy the frosting**: If your cake has frosting, take a moment to appreciate the texture and flavor. You can use your fork or your fingers to spread the frosting around your mouth.
7. **Add toppings (optional)**: If your cake has toppings like nuts, sprinkles, or fresh fruit, you can add them to your bite as you like.
8. **Repeat and enjoy**: Continue taking bites of your cake, enjoying the experience and the flavors. You can also share your cake with others or save some for later.

Some additional tips to keep in mind:

* Be gentle when handling delicate cakes or cupcakes to avoid breaking or crushing them.
* Use a fork to help guide the cake into your mouth if it's particularly messy or crumbly.
* Don't be afraid to get a little messy – cake is meant to be enjoyed, and a little bit of crumbs or frosting on your fingers is part of the fun!
* Consider pairing your cake with a beverage, like coffee, tea, or hot chocolate, to enhance the flavor and texture.    

Now, go ahead and indulge in your delicious cake! ```

