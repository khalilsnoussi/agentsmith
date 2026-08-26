from pydantic import BaseModel
from typing import Any
from .generation import Generation




class LLMResult:

    generations : list[
        list[Generation]
    ]
    llm_output : dict[str, Any]