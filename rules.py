def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I’m doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBot — your friendly Python assistant!"
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I can answer simple questions like your name, time, or greetings!"
    else:
        return "I'm sorry, I don't understand that yet."
