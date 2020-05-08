"""
Серверное приложение для соединений
"""
import asyncio
from asyncio import transports


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.login = None

    def data_received(self, data: bytes):
        decoded = data.decode()
        print(decoded)

        if self.login is None:
            # login:User
            flag : bool = True
            if decoded.startswith("login:"):
                login = decoded.replace("login:", "").replace("\r\n", "")
                for client in self.server.clients:
                    if login == client.login:
                        self.transport.write(f"Логин {client.login} занят, попробуйте другой".encode())
                        flag = False
                        self.connection_lost()
                self.login = decoded.replace("login:", "").replace("\r\n", "")

                # if flag:
                #     self.transport.write(
                #         f"Привет, {self.login}!".encode()
                #     )
                #     self.send_history()
                self.transport.write(
                    f"Привет, {self.login}!".encode()
                )
                self.send_history()
        else:
            self.send_message(decoded)

    def send_message(self, message):
        format_string = f"<{self.login}> {message}"
        self.server.messages.append(f"\r\n{format_string}")
        encoded = format_string.encode()

        for client in self.server.clients:
            if client.login != self.login:
                client.transport.write(encoded)

    def connection_made(self, transport: transports.Transport):
        self.transport = transport
        self.server.clients.append(self)
        print("Соединение установлено")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Соединение разорвано")

    def send_history(self):
        messages = self.server.messages
        i = 0
        messages.reverse()
        for message in messages:
            if i == 10:
                break
            encoded = message.encode()
            self.transport.write(encoded)
            i = i + 1


class Server:
    clients: list

    def __init__(self):
        self.clients = []
        self.messages = []

    def create_protocol(self):
        return ClientProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.create_protocol,
            "127.0.0.1",
            8888
        )

        print("сервер запущен...")

        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")