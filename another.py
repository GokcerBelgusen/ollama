from langchain.callbacks.base import BaseCallbackHandler
from langchain_ollama import OllamaLLM
from pathlib import Path

class StreamingCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.partial_output = ""

    def on_llm_new_token(self, token: str, **kwargs: any) -> None:
        self.partial_output += token
        print(token, end="", flush=True)

llm = OllamaLLM(model="gemma2:2b", callbacks=[StreamingCallbackHandler()])

question = "Uzay-zaman örtüsü nedir ? Kütle çekimi ile nasıl bir ilişkisi vardır ?" 

response = llm.invoke(question)
