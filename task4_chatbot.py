"""
CodeAlpha Internship - Python Programming
TASK 4: Basic Chatbot

"""

import string

# ============================================================
# USER INPUT
# ============================================================

def clean_text(text):
    """Remove punctuation and extra spaces, convert to lowercase."""
    text = text.strip().lower()
    # Remove common punctuation but keep internal spaces
    return text.translate(str.maketrans('', '', string.punctuation))


# ============================================================
# CHATBOT RESPONSE FUNCTION
# ============================================================

def get_response(message):
    cleaned = clean_text(message)

    # ---- GREETINGS ----
    if cleaned in ["hello", "hi", "hey", "hola"]:
        return "Hi! Welcome to CodeAlpha."

    # ---- HOW ARE YOU ----
    elif "how are you" in cleaned or "how're you" in cleaned:
        return "I'm fine, thanks! How can I help you?"

    # ---- GOODBYE ----
    elif cleaned in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    # ---- THANKS ----
    elif "thank" in cleaned or "thanks" in cleaned:
        return "You're welcome!"

    # ---- HELP ----
    elif cleaned == "help":
        return "You can say hello, how are you, or bye."

    # ---- NAME ----
    elif "name" in cleaned:
        return "I'm CodeAlphaBot, your virtual assistant."

    # ---- FALLBACK ----
    else:
        return "Sorry, I don't understand that. Try 'hello' or 'how are you'."


# ============================================================
# RUN CHATBOT
# ============================================================

def run_chatbot():
    print("=" * 50)
    print("CODEALPHA - BASIC CHATBOT")
    print("=" * 50)
    print("\nChatbot: Hi! Welcome to the CodeAlpha chatbot.")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        # Exit if user says bye (also checked in get_response, but we double‑check)
        if clean_text(user_input) in ["bye", "goodbye", "exit", "quit"]:
            break

    print("\nChatbot session ended.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    run_chatbot()