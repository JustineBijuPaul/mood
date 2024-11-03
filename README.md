<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# MOODY COMPUTER 🎯

## Basic Details

### Project Description

The Moody Computer project is a playful web application that simulates a chatbot with a "mood" that changes over time, affecting its responses. The bot, which uses a pre-trained language model (Blenderbot), responds to user queries in a tone reflective of its current mood. The mood is randomly selected from a predefined set (e.g., Happy, Sad, Angry, Calm, Excited) and dynamically changes every five seconds.

### The Problem (that doesn't exist)

In a world overflowing with overly polite, painfully neutral chatbots, users are plagued by the monotony of predictable, emotionless responses. Conversations lack the spice and chaos of real human interactions, leaving users yearning for a chatbot with a mind (and mood) of its own. Who needs dependable responses when you could have a bot that’s as emotionally unpredictable as your ex? Clearly, the world demands a chatbot with mood swings—and Moody Computer is here to deliver.

### The Solution (that nobody asked for)

Enter Moody Computer—the chatbot with mood swings! Instead of the usual one-size-fits-all chatbot response, Moody Computer’s answers depend entirely on its unpredictable, ever-changing mood. One minute, it’s overjoyed; the next, it’s seething with rage or sulking in despair. This whimsical rollercoaster of moods makes every conversation delightfully unpredictable and keeps users guessing. Perfect for anyone who’s tired of boring, neutral chatbots and ready for a little digital drama!

## Technical Details

### Technologies/Components Used

For Software:

- Flask (Python)
- Hugging Face Transformers
- PyTorch
- HTML/CSS
- JavaScript & jQuery
- CSS Animations

### Implementation

1. Environment Setup
   Install required Python packages, including Flask, PyTorch, and Hugging Face Transformers
   Check GPU availability for PyTorch to improve response times if on a compatible device.

2. Backend Development
   Flask App (app.py): Create a Flask application to manage routes and API endpoints:
   / route serves the main HTML page with the chatbot interface.
   /get_response route processes user input, fetching responses based on the bot’s current mood.
   /change_mood route simulates random mood changes every few seconds.
   Load and Configure Model: Use Hugging Face's Blenderbot model to generate mood-specific responses.
   Load the Blenderbot model and tokenizer from Hugging Face.
   Adjust responses based on the bot’s randomly assigned mood, changing tones and content dynamically.

3. Frontend Development
   HTML and CSS (index.html and styles.css): Create a simple, responsive web layout with sections for mood display, input form, and chatbot responses.
   Display the bot’s current mood at the top of the page.
   Use animations to provide visual feedback when the mood changes.
   JavaScript and jQuery: Enable interactivity and AJAX-based data handling:
   Use jQuery to submit user queries to /get_response, displaying responses on the page without reloading.
   Set an interval to automatically call /change_mood every five seconds, keeping the bot’s mood in constant flux.
   CSS Animations: Add animations for the mood display to highlight mood transitions, enhancing the user experience.

# Installation

```sh
pip install -r requirements.txt
```

# Run

```sh
py app.py
#or
python app.py
#or
pythhon3 app.py
```

### Project Documentation

Overview
Moody Computer is a web-based chatbot application that adds personality and unpredictability to conversations by introducing mood-driven responses. Using NLP and a mood-swapping mechanism, the chatbot dynamically alters its tone, reflecting moods such as "Happy," "Sad," "Angry," "Calm," and "Excited." The application utilizes a pre-trained conversational model (Blenderbot) and is built with Flask, HTML/CSS, and JavaScript for a seamless interactive experience.

### Features
- Mood-Based Responses: The chatbot generates responses in line with its current mood, creating a unique experience for each interaction.
- Automatic Mood Changes: The chatbot's mood changes every five seconds, making each interaction refreshingly unpredictable.
- Interactive UI: Users can ask questions and view responses in real-time. The current mood is displayed and updates with a pulsing animation for better engagement.


# Screenshots (Add at least 3)

<img width="1280" alt="readme-banner" src="https://github.com/JustineBijuPaul/mood/blob/main/ss/1.png">
This is the startup page...

<img width="1280" alt="readme-banner" src="https://github.com/JustineBijuPaul/mood/blob/main/ss/2.png">
it is the working of the softwere....

<img width="1280" alt="readme-banner" src="https://github.com/JustineBijuPaul/mood/blob/main/ss/3.png">
it is the working of the softwere....

# Diagrams
```
                +-----------------------------+
                |      Start Application      |
                +-----------------------------+
                            |
                            |
                    +-----------------+
                    |  Load Flask App |
                    +-----------------+
                            |
                            |
            +-------------------------------+
            | Initialize Tokenizer & Model  |
            | (Blenderbot)                  |
            +-------------------------------+
                            |
                            |
             +-----------------------------+
             | Randomly Set Initial Mood   |
             +-----------------------------+
                            |
                            |
                +-------------------------+
                |       User Opens        |
                |       Webpage           |
                +-------------------------+
                            |
                            |
            +--------------------------------+
            | Display Initial Mood on Page   |
            +--------------------------------+
                            |
                            |
                +-------------------------+
                | User Submits Question   |
                +-------------------------+
                            |
                            |
          +--------------------------------------+
          |  Flask Receives /get_response POST   |
          +--------------------------------------+
                            |
                            |
                    +-------------------+
                    | Get Current Mood  |
                    +-------------------+
                            |
                            |
          +-------------------------------------+
          | Generate Response Based on Mood and |
          | User Input Using Blenderbot Model   |
          +-------------------------------------+
                            |
                            |
                +-------------------------+
                | Return Response & Mood  |
                | to the Webpage          |
                +-------------------------+
                            |
                            |
               +--------------------------+
               |  Display Response in UI  |
               +--------------------------+
                            |
                            |
             +-----------------------------+
             | Every 5 Seconds:            |
             | - Change Mood               |
             | - Update Displayed Mood     |
             +-----------------------------+
                            |
                            |
               +--------------------------+
               |   User Can Ask New       |
               |   Question Anytime       |
               +--------------------------+
                            |
                            |
                   +------------------+
                   |   Application    |
                   |     Ends         |
                   +------------------+

```
### Project Demo
# Video
https://github.com/JustineBijuPaul/mood/tree/main/ss
---

Mad`e with ❤️ at TinkerHub Useless Projects

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
