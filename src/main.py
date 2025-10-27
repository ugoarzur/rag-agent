from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(
  model="llama3.2",
)

template = """
You are an expert in answering questions about restaurants.

Here are the relevant reviews:
{reviews}

Question: {question}

Please provide a helpful answer based on the reviews above.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

print("=" * 60)
print("Restaurant Reviews Chat")
print("=" * 60)
print("Ask questions about the restaurant based on reviews.")
print("Type 'q' or 'quit' to exit.\n")

while True:
    try:
        question = input("Your question: ").strip()
        
        if question.lower() in ['q', 'quit', 'exit']:
            print("\nGoodbye!")
            break
        
        if not question:
            continue
        
        print("\nSearching reviews...\n")
        docs = retriever.invoke(question)
        
        # Format reviews for better readability
        formatted_reviews = []
        for i, doc in enumerate(docs, 1):
            rating = doc.metadata.get('rating', 'N/A')
            date = doc.metadata.get('date', 'N/A')
            content = doc.page_content
            formatted_reviews.append(
                f"Review {i} (Rating: {rating}/5, Date: {date}):\n{content}"
            )
        
        reviews_text = "\n\n".join(formatted_reviews)
        
        result = chain.invoke({
            "reviews": reviews_text,
            "question": question
        })
        
        print("Answer:")
        print("-" * 60)
        print(result)
        print("-" * 60)
        print()
        
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        break
    except Exception as e:
        print(f"\nError: {e}")
        print("Please try again.\n")
