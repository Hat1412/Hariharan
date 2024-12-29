import streamlit as st

# from helpers import chat, stream_parser
import ollama

PAGE_TITLE = "Streamlit Ollama Chatbot"

ollama_model = "llama3.2"

SYSTEM_PROMPT = f"""You are a helpful chatbot You can can answer questions for users on any topic."""

st.set_page_config(page_title=PAGE_TITLE, initial_sidebar_state="expanded")


st.title(PAGE_TITLE)

system_prompt = f"""You are a helpful chatbot that has access to the following 
                open-source models {ollama_model}.
                You can can answer questions for users on any topic."""


def chat(user_prompt, model):
    stream = ollama.chat(
        model=model,
        messages=[
            {"role": "assistant", "content": system_prompt},
            {"role": "user", "content": f"Model being used is {model}.{user_prompt}"},
        ],
        stream=True,
    )

    return stream


# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        yield chunk["message"]["content"]


with st.sidebar:
    st.markdown("# Chat Options")
    model = st.selectbox("What model would you like to use?", ollama_model)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What would you like to ask?"):

    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("Generating response..."):
        llm_stream = chat(user_prompt, model=model)

        stream_output = st.write_stream(stream_parser(llm_stream))

        st.session_state.messages.append(
            {"role": "assistant", "content": stream_output}
        )
