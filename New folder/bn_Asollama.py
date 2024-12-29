import streamlit as st
import ollama
import json

PAGE_TITLE = "Binomial Nomenclature Chatbot"

st.set_page_config(page_title=PAGE_TITLE, initial_sidebar_state="expanded")
st.title(PAGE_TITLE)

with open("final_data_copy.json", "r") as file:
    DATASET = json.load(file)

system_prompt = f"""You are a helpful chatbot that is trained on a Binomial Nomenclature dataset {DATASET}.
 You can answer questions for users on any topic."""


def chat(user_prompt, model):
    result = ollama.chat(
        model=model,
        messages=[
            {"role": "assistant", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        stream=False,
    )
    return result["message"]["content"]


# sets up sidebar nav widgets
with st.sidebar:
    st.markdown("# Chat Options")
    model = st.selectbox("What model would you like to use?", ["llama3.2"])

# checks for existing messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What would you like to ask?"):
    # Display user prompt in chat message widget
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # adds user's prompt to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("Generating response..."):
        # retrieves response from model
        response = chat(user_prompt, model)

        # Display assistant response in chat message widget
        with st.chat_message("assistant"):
            st.markdown(response)

        # appends response to the message list
        st.session_state.messages.append({"role": "assistant", "content": response})
