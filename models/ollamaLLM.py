from ollama import Client
from .base import BaseLLM
from typing import Literal, Mapping, Any, Iterator, override, overload
from pydantic import PrivateAttr, BaseModel
from outputs import LLMResult



class OllamaLLM(BaseLLM):

    def __init__(self,
                model : str,
                reasoning : bool = False,
                streaming : bool = True,
                base_url : str = "http://localhost:11434",
                ):
        self.model = model
        self.reasoning = reasoning
        self.base_url = base_url
        self._client = Client(host = base_url)
        self._stream = streaming
    
    def _generate(
            self,
            prompt : str,
    ) -> Iterator[Mapping[str, Any] | str]:
        #self._client.chat()
        yield from self._client.generate(
            model = self.model,
            prompt = prompt,
            stream = self._stream,
            think = self.reasoning
        )

    def generate(self, prompt : str) -> Mapping[str, Any]:
        return self._client.generate(
            model = self.model,
            prompt = prompt,
            stream = self._stream,
            think = self.reasoning
        )


    def bing_tools(tools : list[]) -> None:
        return 


    def stream(self, prompt : str):
        flag = False
        generation_iterator = self._generate(prompt = prompt)
        while not flag:
            response = next(generation_iterator)
            yield response['response']
            flag = response['done']
        