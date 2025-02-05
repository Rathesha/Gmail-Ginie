import google.generativeai as genai
import tkinter as tk

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyCS0C8fmXwf6k8b4Mi5ZPiIHyqJDaSGqKk")

# Initialize the chat model
model = genai.GenerativeModel("gemini-pro")
chat_session = model.start_chat()

def chatbot_response(user_input):
    try:
        response = chat_session.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Function to handle user input and bot response
def on_send_button_click():
    user_input = entry.get()  # Get input from the user
    if user_input.lower() == "exit":
        root.quit()  # Exit the chatbot on "exit"
    response = chatbot_response(user_input)  # Get bot's response
    chat_box.insert(tk.END, "You: " + user_input + "\n")  # Display user message
    chat_box.insert(tk.END, "Bot: " + response + "\n")  # Display bot message
    entry.delete(0, tk.END)  # Clear input field after sending

# Set up the GUI window
root = tk.Tk()
root.title("Chatbot UI")

# Create a chat box (text area) to display conversation
chat_box = tk.Text(root, height=15, width=50, wrap=tk.WORD)
chat_box.pack(padx=10, pady=10)

# Create an entry box to get user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Create a send button to submit the input
send_button = tk.Button(root, text="Send", command=on_send_button_click)
send_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
