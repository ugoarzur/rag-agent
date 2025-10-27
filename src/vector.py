from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

import os
import pandas as pd
from pathlib import Path


# Get project root directory
project_root = Path(__file__).parent.parent
csv_path = project_root / "assets" / "realistic_restaurant_reviews.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found at {csv_path}")

# Loading data
df = pd.read_csv(csv_path)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = str(project_root / "chroma")
db_exists = os.path.exists(db_location)


if not db_exists:
    print("Creating vector database...")
    documents = []
    ids = []

    for i, row in enumerate(df.itertuples()):
        if i % 100 == 0:
            print(f"Processing row {i}/{len(df)}")
        
        title = str(getattr(row, 'Title', ''))
        review = str(getattr(row, 'Review', ''))
        rating = getattr(row, 'Rating', 0)
        date = str(getattr(row, 'Date', ''))
        
        document = Document(
            page_content=title + " " + review,
            metadata={"rating": rating, "date": date},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
    print(f"Processed {len(documents)} documents")

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if not db_exists:
    print("Adding documents to vector store...")
    vector_store.add_documents(documents, ids=ids)
    print("Vector database created successfully!")
else:
    print(f"Using existing vector database at {db_location}")

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
