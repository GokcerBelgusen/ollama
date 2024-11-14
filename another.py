from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

query = "Tell me a joke"

for chunks in llm.stream(query):
    print(chunks)
