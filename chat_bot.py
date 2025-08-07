import pyautogui
import pyperclip
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_CHATBOT_KEY"))
    
    
# Wait before starting
print("Starting...")
time.sleep(1)

# Step 1: Click the icon to focus WhatsApp Web (optional)
pyautogui.click(x=1200, y=1060)
time.sleep(0.5)

# Step 2: Click at the start of message
pyautogui.moveTo(700, 160)
pyautogui.click()
time.sleep(0.5)

# step 2.5: click at the arrow to move chat down if needed

# Try to locate the arrow button on screen
try:
    arrow_location = pyautogui.locateCenterOnScreen('arrow_down.png', confidence=0.8)
    if arrow_location:
        print("🔽 Arrow found, clicking...")
        pyautogui.click(arrow_location)
        time.sleep(0.5)
    else:
        print("❔ Arrow not found, but no exception was raised.")
except pyautogui.ImageNotFoundException:
    print("❌ Arrow image not found on screen. Continuing without clicking it.")

# Step 3: Hold Shift and click the end of selection
pyautogui.keyDown('shift')
pyautogui.click(x=1880, y=950)
pyautogui.keyUp('shift')
time.sleep(0.5)

# Step 4: Copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.click()

# Step 5: Get text from clipboard
chat_history = pyperclip.paste()
print("Copied from WhatsApp Web:")
print(chat_history)

completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "you are a person named sohaib who speaks urdu as well as english."
        "you are from pakistan and have a fun,cheerfull personality. you analyze chat history."
        "output should be the next chat response as sohaib."},
        {"role": "user", "content": chat_history}
    ]
)

response = completion.choices[0].message.content

# Copy the message to clipboard
pyperclip.copy(response)
time.sleep(0.5)

# Click the chat box
pyautogui.click(x=800, y=1000)
time.sleep(0.5)

# Paste the message
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.3)

# Press Enter to send
pyautogui.press('enter')
