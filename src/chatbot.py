import re

# Function to read the dataset from the file
def load_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pairs = [line.strip().split('\t') for line in lines if '\t' in line]
    return pairs

# Path to the dataset file
file_path = r"C:\Users\sachin\Downloads\archive (7)\dialogs.txt"  # Use raw string to handle backslashes

# Load the dataset
pairs = load_dataset(file_path)

# Create a dictionary for quick response lookup
response_dict = {user_input.lower(): bot_response for user_input, bot_response in pairs}

def get_bot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Simple if-else based responses
    if user_input in response_dict:
        return response_dict[user_input]
    
    # Pattern matching for more complex queries
    elif re.search(r'hi|hello|hey', user_input, re.IGNORECASE):
        return "Hello! How can I help you today?"
    elif re.search(r'how are you', user_input, re.IGNORECASE):
        return "I'm just a bot, but I'm here to help you!"
    elif re.search(r'what is your name', user_input, re.IGNORECASE):
        return "I'm a simple rule-based chatbot."
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"

# Define the chatbot function to interact with users
def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        bot_response = get_bot_response(user_input)
        print(f"Chatbot: {bot_response}")

# Running the chatbot
if __name__ == "__main__":
    chatbot()
