import random
import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Define response patterns with more variety
    responses = {
        'greetings': [
            "Hello! 👋 How can I help you today?",
            "Hi there! 🌟 What can I do for you?",
            "Hey! 😊 Great to see you!",
            "Greetings! 🎉 How's your day going?"
        ],
        'how_are_you': [
            "I'm doing great! Thanks for asking! 😊",
            "I'm just a bot, but I'm having a wonderful day! 🌈",
            "All systems running smoothly! How about you? ⚡",
            "I'm fantastic! Ready to help you with anything! 🚀"
        ],
        'name': [
            "I'm ChatBot, your friendly AI assistant! 🤖",
            "You can call me ChatBot! I'm here to help! 💬",
            "I'm ChatBot, powered by Python and ready to chat! 🐍"
        ],
        'time': [
            f"The current time is {datetime.now().strftime('%H:%M:%S')} ⏰",
            f"It's {datetime.now().strftime('%I:%M %p')} right now! 🕐",
            f"Current time: {datetime.now().strftime('%H:%M:%S')} 📅"
        ],
        'date': [
            f"Today is {datetime.now().strftime('%A, %B %d, %Y')} 📅",
            f"The date is {datetime.now().strftime('%B %d, %Y')} 🗓️",
            f"It's {datetime.now().strftime('%A')}, {datetime.now().strftime('%B %d')} 📆"
        ],
        'bye': [
            "Goodbye! Have an amazing day! 🌟",
            "See you later! Take care! 👋",
            "Farewell! Hope to chat again soon! 💫",
            "Bye! Thanks for the great conversation! 😊"
        ],
        'thanks': [
            "You're very welcome! 😊",
            "My pleasure! Happy to help! 🌟",
            "Anytime! That's what I'm here for! 🤗",
            "Glad I could assist you! 🎉"
        ],
        'help': [
            "I can help with many things! Try asking me about:\n• Time and date\n• Weather (general info)\n• Math calculations\n• Fun facts\n• Or just have a friendly chat! 💡",
            "Here are some things I can do:\n• Tell you the time\n• Answer simple questions\n• Have conversations\n• Provide information\nJust ask me anything! 🎯"
        ]
    }
    
    # Pattern matching with regex for better understanding
    if re.search(r'\b(hello|hi|hey|greetings)\b', user_input):
        return random.choice(responses['greetings'])
    elif re.search(r'\b(how are you|how are you doing|how\'s it going)\b', user_input):
        return random.choice(responses['how_are_you'])
    elif re.search(r'\b(your name|who are you|what are you)\b', user_input):
        return random.choice(responses['name'])
    elif re.search(r'\b(what time|current time|time is it)\b', user_input):
        return random.choice(responses['time'])
    elif re.search(r'\b(what date|today\'s date|current date|date today)\b', user_input):
        return random.choice(responses['date'])
    elif re.search(r'\b(bye|goodbye|see you|farewell)\b', user_input):
        return random.choice(responses['bye'])
    elif re.search(r'\b(thank|thanks|appreciate)\b', user_input):
        return random.choice(responses['thanks'])
    elif re.search(r'\b(help|what can you do|commands)\b', user_input):
        return random.choice(responses['help'])
    
    # Math calculations
    elif re.search(r'\b(calculate|what is|solve)\b.*\d+', user_input):
        try:
            # Simple math expression extraction
            expression = re.sub(r'[^\d\+\-\*\/\.\s]', '', user_input)
            if expression.strip():
                result = eval(expression)
                return f"Let me calculate that for you... The answer is {result}! 🧮"
        except:
            return "I couldn't calculate that. Try a simpler math expression! 🤔"
    
    # Weather-related (basic responses)
    elif re.search(r'\b(weather|temperature|forecast)\b', user_input):
        return "I don't have real-time weather data, but I can tell you that checking a weather app would be your best bet! 🌤️"
    
    # Fun facts
    elif re.search(r'\b(fun fact|interesting fact|tell me something)\b', user_input):
        facts = [
            "Did you know? Honey never spoils! Archaeologists have found 3000-year-old honey that's still edible! 🍯",
            "Bananas are berries, but strawberries aren't! 🍌🍓",
            "Octopuses have three hearts and blue blood! 🐙",
            "A group of flamingos is called a 'flamboyance'! 🦩"
        ]
        return random.choice(facts)
    
    # Jokes
    elif re.search(r'\b(joke|funny|laugh)\b', user_input):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "I told my wife she was drawing her eyebrows too high. She looked surprised! 😂",
            "Why don't eggs tell jokes? They'd crack each other up! 🥚",
            "What do you call a fake noodle? An impasta! 🍝"
        ]
        return random.choice(jokes)
    
    # Default response with more personality
    else:
        default_responses = [
            "That's interesting! Tell me more about that. 🤔",
            "I see! Could you explain that differently? 💭",
            "Hmm, I'm not sure I understand. Could you rephrase that? 🧐",
            "Interesting thought! What else would you like to discuss? 💡",
            "I'm still learning! Could you help me understand that better? 📚"
        ]
        return random.choice(default_responses)
