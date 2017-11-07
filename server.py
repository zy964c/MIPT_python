import asyncio

def run_server(host, port):
    """
    runs server
    """
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

class ClientServerProtocol(asyncio.Protocol):
    """
    ClientServerProtocol
    """
    def connection_made(self, transport):
        self.transport = transport
        #print(self.transport)

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        print(data)
        return data
