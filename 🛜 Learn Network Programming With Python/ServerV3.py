import asyncio

async def process_request(data):
    await asyncio.sleep(1) # Simulate IO Operation
    return data[::-1]

async def handle_client(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Recieved {message} from {addr}")
    
    response = await process_request(message)
    print(f"Sending: {response} to {addr}")
    writer.write(response.encode())

    await writer.drain()
    writer.close()

async def server():
    sever = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Serving on port {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(server())