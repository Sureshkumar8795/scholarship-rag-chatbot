import streamlit as st
import pandas as pd
import csv
import os

from retriever import retrieve_context
from llm import generate_answer

st.set_page_config(
    page_title="Scholarship RAG Chatbot",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Analytics File
# -----------------------------
CHAT_LOG = "chat_history.csv"

if not os.path.exists(CHAT_LOG):
    with open(CHAT_LOG, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["question"])

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🎓 Scholarship Assistant")

    st.success("Knowledge Base Loaded")

    language = st.selectbox(
        "Language",
        ["English", "Tamil"]
    )

    st.markdown("---")

    st.header("Eligibility Checker")

    category = st.selectbox(
        "Category",
        ["SC", "ST", "BC", "MBC", "Minority", "General"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    course = st.selectbox(
        "Course",
        [
            "Engineering",
            "Science",
            "Arts",
            "Medical",
            "Polytechnic"
        ]
    )

    income = st.number_input(
        "Family Income (₹)",
        min_value=0,
        value=100000
    )

    if st.button("Check Eligibility"):

        eligibility_query = f"""
        I am a {gender} student.

        Category: {category}

        Course: {course}

        Family Income: {income}

        Which scholarships can I apply for?
        """

        context_chunks = retrieve_context(
            eligibility_query,
            top_k=5
        )

        context = "\n\n".join(context_chunks)

        answer = generate_answer(
            context,
            eligibility_query
        )

        st.markdown("### Recommended Scholarships")

        st.write(answer)

# -----------------------------
# Main Title
# -----------------------------
st.title("🎓 Scholarship RAG Chatbot")

st.caption(
    "Tamil Nadu & India Scholarship Assistant"
)

# -----------------------------
# Suggested Questions
# -----------------------------
st.subheader("Suggested Questions")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "What scholarships are available for SC students?"
    )

    st.info(
        "What documents are required for BC scholarship?"
    )

with col2:
    st.info(
        "How do I apply through NSP?"
    )

    st.info(
        "What scholarships are available for female students?"
    )

st.markdown("---")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
question = st.chat_input(
    "Ask a scholarship question..."
)

if question:

    with open(
        CHAT_LOG,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)
        writer.writerow([question])

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching..."):

            context_chunks = retrieve_context(
                question,
                top_k=5
            )

            context = "\n\n".join(context_chunks)

            final_question = f"""
            Answer in {language}.

            Question:
            {question}
            """

            answer = generate_answer(
                context,
                final_question
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# -----------------------------
# Analytics Dashboard
# -----------------------------
st.markdown("---")

st.subheader("📊 Analytics Dashboard")

try:

    df = pd.read_csv(CHAT_LOG)

    total_questions = len(df)

    st.metric(
        "Total Questions Asked",
        total_questions
    )

    if total_questions > 0:

        sc_queries = df[
            df["question"].str.contains(
                "SC",
                case=False,
                na=False
            )
        ].shape[0]

        female_queries = df[
            df["question"].str.contains(
                "female",
                case=False,
                na=False
            )
        ].shape[0]

        nsp_queries = df[
            df["question"].str.contains(
                "NSP",
                case=False,
                na=False
            )
        ].shape[0]

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "SC Queries",
            sc_queries
        )

        c2.metric(
            "Female Scholarship Queries",
            female_queries
        )

        c3.metric(
            "NSP Queries",
            nsp_queries
        )

except Exception:
    st.info("Analytics will appear after users ask questions.")