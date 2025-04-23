import asyncio

async def tcp_client(request):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print(f"Sending {request}")
    writer.write(request.encode())

    response = await reader.read(1024)
    print(f"Received: {response.decode()}")

    writer.close()
    await writer.wait_close()

asyncio.run(tcp_client(" Hello, Async Programming World!"))