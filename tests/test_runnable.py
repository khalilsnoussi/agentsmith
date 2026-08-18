import pytest
from core import Runnable 
from typing import override
import time

class TestRunnable(Runnable[str, str]):
    def invoke(self, input : str) -> str:
        time.sleep(4)
        return 'hello, world'



def test_invoke():
    runnable = TestRunnable()
    result = runnable.invoke(input = 'hello')
    assert result == 'hello, world'


