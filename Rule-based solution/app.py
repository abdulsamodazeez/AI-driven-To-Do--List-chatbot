import streamlit as st
from todochat  import ToDoChatbot  # Import your ToDoChatbot class

# Initialize the chatbot
chatbot = ToDoChatbot()

st.title("ToDo Chatbot")

# User input
user_input = st.text_input("Enter your command:", key="user_input")

if user_input:
    # Process the command
    response = chatbot.respond(user_input)
    st.write(f"{chatbot.name}: {response}")

    # Optional: Display the current state of lists
    st.subheader("Current To-Do Lists")
    for list_name, tasks in chatbot.lists.items():
        st.write(f"**{list_name}**: {', '.join(tasks) if tasks else 'No tasks yet.'}")
