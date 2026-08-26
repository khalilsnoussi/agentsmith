from typing import Any, Literal



class Generation:
    text : str
    generation_info : dict[str, Any] | None = None
    type : Literal["Generation"] = "Generation"