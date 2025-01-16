import pyautogui           # For automating GUI actions like mouse clicks, drags, and keystrokes.(tells cursor position)
import time                # To introduce delays between actions for reliability.
import pyperclip           # For accessing and modifying clipboard content. (import text from clipboard)
from openai import OpenAI  # To interact with OpenAI's GPT model.


client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):                   # reply only when last message is from sender

    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]            # Splits the chat log using the delimiter "/2024]" to Extract the last message after splitting the chat log.
    if sender_name in messages:
        return True              # if the sender's name is in the last message.
    return False                 # (for multi line messages identifying by sender)
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1639, 1412)   # Simulates a mouse click at specific screen coordinates to open the Chrome browser

time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(5)
# Infinite Loop: The script continuously monitors the chat every 5 seconds.



    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(972,202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1994, 281)             # deselect the text by again clicking somewhere else in the chat

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))                          # call fnction to check reply only when last message is from sender
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(                          # if yes, generates a response using OpenAI's GPT model.
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)                     # Copies the generated response to the clipboard.

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)            # Clicks the chat input box to focus it.
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text or the response copied to the clipboard.
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter to send the message
        pyautogui.press('enter')         # reply like harry and send it


''' Purpose :
Automates a chatbot that monitors a web-based chat application.
Responds to messages from a specific sender with witty and humorous replies.
Ensures the assistant only responds when appropriate (last message from the sender).
'''        
