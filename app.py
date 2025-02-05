import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCS0C8fmXwf6k8b4Mi5ZPiIHyqJDaSGqKk")

# Streamlit UI
st.title("💬 Gemini Chatbot")
st.write("Ask me anything!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Append user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response from Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    bot_response = response.text if response else "Sorry, I couldn't process that."
    
    # Append bot response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
