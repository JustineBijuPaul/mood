import random
import time
import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Define moods
moods = ["happy", "sad", "angry", "calm", "excited"]

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize the tokenizer and model
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill").to(device)

def get_mood():
    """
    Simulate mood swings by randomly selecting a mood.
    """
    return random.choice(moods)

def get_response(mood, user_input):
    """
    Get a response based on the current mood using a pre-trained model.
    """
    prompt = f"In a {mood} mood, respond to: '{user_input}'"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    response_ids = model.generate(inputs["input_ids"], max_length=100, do_sample=True, top_k=50)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    # Remove the prompt from the generated text
    response = response.replace(prompt, "").strip()
    return response

def main():
    """
    Main function to simulate mood swings over time and respond to user input.
    """
    current_mood = get_mood()
    print(f"Initial mood: {current_mood}")

    while True:
        time.sleep(5)  # Wait for 5 seconds before changing mood
        new_mood = get_mood()
        if new_mood != current_mood:
            print(f"Mood changed from {current_mood} to {new_mood}")
            current_mood = new_mood

        # Check for user input
        user_input = input("Ask me something: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = get_response(current_mood, user_input)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
