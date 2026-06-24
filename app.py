import streamlit as st

from retriever import retrieve_context
from llm import generate_answer

st.set_page_config(
    page_title="Scholarship RAG Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Scholarship RAG Chatbot")
st.caption(
    "Tamil Nadu & India Scholarship Assistant"
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input(
    "Ask a scholarship question..."
)

if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant
    with st.chat_message("assistant"):

        with st.spinner("Searching scholarships..."):

            context_chunks = retrieve_context(
                question,
                top_k=5
            )

            context = "\n\n".join(
                context_chunks
            )

            answer = generate_answer(
                context,
                question
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )