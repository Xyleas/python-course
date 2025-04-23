import asyncio

async def hello_world():
    print("Hello ")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello_world())