from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(
  model="llama3.2",
)

template = """
Your are an expert in answering question about restaurant.

Here is the reviews: {reviews}

Here is a the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print('\n')
    question = input("\nAsk a question about the restaurant: ")
    print('\n')
    if question == 'q':
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({
      "reviews": reviews,
      "question": question
    })
    print(result)
