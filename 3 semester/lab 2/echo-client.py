import socket
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         message = input("Введите сообщение:")
#         if message.lower() == "exit" or message.lower() == "выход":
#             break
#         s.sendall(message.encode())
#         data = s.recv(1024)
# print(f"Received {data!r}")

import asyncio

HOST = "127.0.0.1"
PORT = 34561

async def client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    try:
        while True:
            message=input("Введите сообщение: ")
            writer.write(message.encode())
            await writer.drain()
            if message.lower() == "exit" or message.lower() == "quit" or message.lower() == "выход":
                break
            data=await reader.read(1024)
            print(f'Сервер повторил: {data.decode()}')
    finally:
        writer.close()
        await writer.wait_closed()
        print("Отключение от сервера")

asyncio.run(client())