from core import Runnable
from typing import override
import time
import asyncio

class MyRunnable(Runnable[str, str]):


    @override
    def invoke(self, input : str)->str:
        time.sleep(2)
        print(input)
        return input[0]


test_inputs = ['hello', 'HELLOOO', 'KOKO']
test_runnable = MyRunnable()
# print(test_runnable.invoke('hello'))
# start=  time.time()
# values = test_runnable.batch(inputs = test_inputs)
# end = time.time()
# print(f'duration is {end-start}')
# print(values)

async def main():
    return await test_runnable.abatch(inputs = test_inputs)

start= time.time()
asyncio.run(main())
end = time.time()
print(f'duration is {end-start}')