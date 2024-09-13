import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I am doing great, thank you! How can I assist you today?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries!",]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day!"]
    ]
]

def chatbot():
    print("Hello! I am your chatbot. Type 'quit' to exit.")
    # Initialize the chatbot with predefined pairs
    chat = Chat(pairs, reflections)
    # Start the conversation
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
