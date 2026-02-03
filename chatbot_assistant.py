# Define a dictionary with rules and responses
rules = {
    'hello': 'Hi! How can I assist you today?',
    'hi': 'Hello! It\'s nice to meet you.',
    'how are you': 'I\'m doing great, thanks for asking!',
    'who are you': 'I\'m an AI assistant developed by Hemanth.',
    'what is your name': 'I\'m an AI assistant developed by Hemanth.',
    'what can you do': 'I can assist with a wide range of tasks, including answering questions, generating text, and completing tasks.',
    'tell me a joke': 'Why was the math book sad? Because it had too many problems.',
    'goodbye': 'It was nice chatting with you! Have a great day!',
    'thanks': 'You\'re welcome!',
    'thank you': 'You\'re welcome!',
    'default': 'Sorry, I didn\'t understand that. Please try again!'
}

# Define a list of keywords for more advanced responses
keywords = {
    'math': ['math', 'algebra', 'geometry', 'calculus'],
    'science': ['science', 'biology', 'chemistry', 'physics'],
    'programming': ['programming', 'python', 'java', 'c++'],
    'history': ['history', 'ancient', 'medieval', 'modern']
}

# Define a dictionary with more advanced responses
advanced_responses = {
    'math': 'I can help with math-related tasks, such as solving equations or graphing functions.',
    'science': 'I can assist with science-related topics, such as explaining concepts or providing information on various fields.',
    'programming': 'I can help with programming-related tasks, such as writing code or debugging issues.',
    'history': 'I can provide information on historical events or periods.'
}

def chatbot(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    
    # Check if user input matches any of the predefined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response
    
    # Check if user input contains any of the keywords
    for keyword, keywords_list in keywords.items():
        for keyword_item in keywords_list:
            if keyword_item in user_input:
                return advanced_responses[keyword]
    
    # If no match is found, return the default response
    return rules['default']

# Test the chatbot
while True:
    user_input = input('User: ')
    print('Chatbot:', chatbot(user_input))

