from core import Runnable
from abc import ABC, abstractmethod
from typing import override


class BaseLLM(Runnable):


    @override
    def invoke(self, input : str) -> str:
        output = self.generate(prompt=input)
        return output['response']
    
    @abstractmethod
    def _generate(self, prompt : str):
        """the internal mechanism of generation
            should be handled by each LLM provider
            openai, ollama, anthropic, deepseek, kimi
        """
        ...

    @abstractmethod
    def generate(self, prompt : str):
        ...