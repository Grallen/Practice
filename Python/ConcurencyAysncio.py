#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Concurrency Challenge (Asyncio)
# Write an asynchronous function fetch_data that simulates fetching data from multiple APIs with varying delays. Use asyncio.gather to run them concurrently and return results in the order of completion.
# Simulated API calls with asyncio.sleep
# Input: ["api1", "api2", "api3"]
# Output: ["data from api2", "data from api1", "data from api3"] (based on completion order)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import asyncio
import random
random.seed()

async def fakeapi(api):
    x = random.randint(1,10)
    await asyncio.sleep(x)
    return x, f"DATA Waited {x}: ({api})"


async def main(*apis):
    tasks = [fakeapi(api) for api in apis]
    results = await asyncio.gather(*tasks)
    results.sort(key=lambda x: x[0])
    for result in results:
        print(result)

asyncio.run(main("AAA","BBB","CCC","DDD","EEE"))


# OUTPUT
# (1, 'DATA Waited 1: (CCC)')
# (2, 'DATA Waited 2: (AAA)')
# (2, 'DATA Waited 2: (DDD)')
# (3, 'DATA Waited 3: (BBB)')
# (3, 'DATA Waited 3: (EEE)')
# 
# [Execution complete with exit code 0]
