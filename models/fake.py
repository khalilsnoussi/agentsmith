from models import BaseLLM
from typing import override
import time




class FakeLLM(BaseLLM):

    @override
    def _generate(self, prompt : str, response : str):
        time.sleep(5) ### we simulate the processing time of an LLM
        return response
        
    