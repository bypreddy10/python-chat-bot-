from flask import Flask, render_template, request, jsonify
from rules import chatbot_response
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route("/")
def home():
    """Render the main chat interface."""
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    """Handle chat messages and return bot responses."""
    try:
        user_input = request.form.get("msg", "").strip()
        
        if not user_input:
            return jsonify({"response": "Please type a message! 💬"})
        
        # Log user input for debugging
        logger.info(f"User input: {user_input}")
        
        # Get response from chatbot
        response = chatbot_response(user_input)
        
        # Log bot response
        logger.info(f"Bot response: {response}")
        
        return jsonify({"response": response})
    
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return jsonify({"response": "Sorry, I encountered an error processing your message. Please try again! 🔄"})

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run the Flask app with enhanced configuration
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
