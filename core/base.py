from abc import ABC, abstractmethod
from typing import TypeVar, Generic, cast
import asyncio
import json
from concurrent.futures import ThreadPoolExecutor


Input = TypeVar('Input')
Output = TypeVar('Output')



class Runnable(ABC, Generic[Input, Output]):

    @abstractmethod
    def invoke(self, input : Input) -> Output:
        """Process input and returns the result"""


    async def ainvoke(self, input : Input) -> Output:
        return await asyncio.get_running_loop().run_in_executor(
            None,
            self.invoke,
            input
        )

    def batch(self, inputs : list[Input]) -> list[Output]:
        """running invoke in parallel over all the inputs"""
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = executor.map(self.invoke, inputs)
            return cast('list[Output]', list(futures))

    async def abatch(self, inputs : list[Input]) -> list[Output]:
        coroutines = map(self.ainvoke, inputs)
        return await asyncio.gather(*coroutines)

    def serialize(self):
        pass
