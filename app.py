import random
import time
import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from flask import Flask, render_template, request, jsonify

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

app = Flask(__name__)

# Global variable to store the current mood
current_mood = get_mood()

@app.route('/')
def index():
    return render_template('index.html', mood=current_mood)

@app.route('/get_response', methods=['POST'])
def get_response_route():
    global current_mood
    user_input = request.form['user_input']
    response = get_response(current_mood, user_input)
    return jsonify({'response': response, 'mood': current_mood})

@app.route('/change_mood', methods=['POST'])
def change_mood():
    global current_mood
    new_mood = get_mood()
    current_mood = new_mood
    return jsonify({'mood': current_mood})

if __name__ == "__main__":
    app.run(debug=True)
