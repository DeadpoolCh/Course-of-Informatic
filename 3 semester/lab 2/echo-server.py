# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind((HOST, PORT))
#     s.listen(1)
#     print(f"Сервер прослушивается на {HOST}:{PORT}")
#     conn, addr = s.accept()
#     with conn:
#         print(f"Соединение с {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             message = data.decode()
#             print(f"Ввод пользователя: {message}")
#             if message.lower() == "exit" or message.lower() == "выход":
#                 print("Закрытие соединения...")
#                 break
#             conn.sendall(message.encode())
#         print("Соединение закрыто")

import socket
import asyncio

HOST = "127.0.0.1"
PORT = 34561

clients=set()

def isDNA(seq:str)-> str:
    return 'Is a DNA' if set(seq.upper()).issubset(set('GATCRYWSMKHBVDN')) else 'Not a DNA'

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername') # возвращает адрес клиента
    print(f"Подключение к {addr}")
    clients.add(writer)

    try:
        while True:
            data = await reader.read(1024) # Данные от клиента
            if not data:
                break # Клиент отключился без данных
            message = data.decode().strip()
            print(f"Получено сообщение с {addr}: {message}")
            if message == "exit" or message == "выход" or message == "quit":
                print(f'Соединение с {addr} закрыто')
                break
            response=isDNA(message)
            writer.write(response.encode())
            await writer.drain()
    except asyncio.CancelledError:
        pass
    finally:
        writer.close()
        await writer.wait_closed()
        clients.remove(writer)
        print(f"Отключен от {addr}")

async def main():
    server = await asyncio.start_server(handle_echo, HOST, PORT)
    print(f'Сервер запущен на {HOST}:{PORT}')
    async with server:
        await server.serve_forever() # Ожидание клиентов

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Сервер завершает работу...')
    for client in clients:
        client.close()
