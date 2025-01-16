# This script uses OpenAI's GPT-3.5 API to interact with a virtual assistant persona named "Jarvis."

from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
   api_key="sk-proj-WxS17ehGk2PnwmzCHcDwT3BlbkFJFj6bYTk9jG1bqZaFTej",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",         # Specifies the AI model.
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

# role: system: Sets the assistant's persona and skills. In this case, "Jarvis" is positioned as a virtual assistant knowledgeable in tasks similar to Alexa and Google Cloud.
# role: user: Represents the user's input/question ("what is coding").

print(completion.choices[0].message.content)

# Extracts and prints the AI's response.
# completion.choices[0].message.content retrieves the assistant's reply.


'''
The method call client.chat.completions.create() interact with the OpenAI language model (in this case, GPT-3.5) and generate a conversational response.

client: Represents the connection to OpenAI's API using your credentials (API key).
chat: Indicates you're working with the Chat Completions endpoint, specifically designed for handling conversations and chat-style interactions.
completions: This submodule handles the core functionality of generating text completions (responses) from the model.
create: The method that executes the request and generates the response based on input parameters.

The modular structure helps developers clearly distinguish between different endpoints (e.g., edits, images, or chat) and functionalities.

The Chat API is tailored to handle conversation-like interactions. Unlike the older completions endpoint, 
chat.completions uses a format (messages) that supports multi-turn conversations with roles like system, user, and assistant.

Splitting it into chat, completions, and create allows for future scalability. For example, OpenAI might expand chat-related features under the chat module.

Using create clarifies that this method generates a new response, differentiating it from methods like list (to retrieve historical completions) or delete (to manage resources).

'''


# How It Works in Practice

'''
1.API Interaction
Your request, including the model, messages, and other parameters, is sent to OpenAI's servers.

2.OpenAI's model processes the input data:
Understands the system role to establish context (assistant persona or behavior).
Analyzes the user message to generate a relevant and coherent response.

3.The API responds with a JSON object containing:
The choices array, where each element is a possible completion.
Metadata like token usage and model version.

4.The create method processes the API's response into a Python object for easier manipulation.
'''


# Why This Structure Is Important

'''
Clarity and Readability
A hierarchical structure (chat.completions.create) is easier to read and understand, making development more intuitive.

Reusability
The modular design allows developers to use the same base client (OpenAI) for different tasks (e.g., generating text, handling chat-based interactions, or creating edits).

Scalability
As OpenAI evolves, this structure enables seamless addition of new features or endpoints without breaking existing integrations.
'''