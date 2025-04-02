from app.browser_control import perform_action
from transformers import pipeline

# Load local Hugging Face model once on startup
llm = pipeline("text2text-generation", model="google/flan-t5-base")

async def interact(command: str):
    try:
        prompt = f"Translate this into browser automation steps: {command}"
        result = llm(prompt, max_length=100)[0]["generated_text"]
        print("Translated command:", result)

        # Pass the interpreted instruction to the action layer
        return await perform_action(result)

    except Exception as e:
        print("Error in local model:", str(e))
        return {"status": "error", "message": str(e)}
