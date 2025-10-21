# Notes

Building a local RAG Agent with Langchain.

## Semantic search is done by:

1. **Load:** loading data is done with [**Document Loaders**](https://docs.langchain.com/oss/python/langchain/retrieval#document_loaders)
2. **Split:** breaking data into smaller chunks thanks to [**Text Splitters**](https://docs.langchain.com/oss/python/langchain/retrieval#text_splitters) . Enable indexing data and passing data to the model. The smaller the chunk, the easier it is to use it in context window.
3. **Store:** Store and index splits using [**Vector Stores**](https://docs.langchain.com/oss/python/langchain/retrieval#vectorstores) and [**Embeddings**](https://docs.langchain.com/oss/python/langchain/retrieval#embedding_models).

## Run

You will need [uv](https://docs.astral.sh/uv/getting-started/installation/) as package manager.

```bash
uv venv # create virtual env
uv sync
uv run src/main.py
```

Then ask your questions on the restaurant reviews.
Once you are done, press `q` as response to quit.

# Resources

- [Youtube: Local AI Agent with Python (Ollama, Langchain, RAG)](https://youtu.be/E4l91XKQSgw?si=gM9_329Rf2GZe-nX)
- [Docling Documentation](https://docling-project.github.io/docling/usage/)
