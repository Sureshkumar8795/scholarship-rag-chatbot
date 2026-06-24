from retriever import retrieve_context
from llm import generate_answer

def main():

    while True:

        question = input("\nAsk a question (or type exit): ")

        if question.lower() == "exit":
            break

        retrieved_chunks = retrieve_context(
            question,
            top_k=3
        )

        context = "\n\n".join(retrieved_chunks)

        answer = generate_answer(
            context,
            question
        )

        print("\nAnswer:")
        print(answer)

if __name__ == "__main__":
    main()