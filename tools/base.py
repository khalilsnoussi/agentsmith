from core import Runnable
from typing import Any, override, Callable
import inspect

def _google_arg_descriptions(fn : Callable) -> dict[str, str]:
    docs = inspect.getdoc(fn) or ""
    return docs



class BaseTool(Runnable[str | dict[str, Any], Any]):
    """Base class for all AgentSmith tools.
    
    This abstract class defines the interface that all AgentSmith tools must implement.

    Tools are component that can be called by agents to perform specific actions.
    """

    @override
    def invoke(self, input):
        ...


    def run(self, input):
        ...



    def _run(self, input):
        ...
