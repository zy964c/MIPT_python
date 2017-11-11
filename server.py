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
    storage = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode(encoding='utf_8'))
        self.transport.write(resp.encode(encoding='utf_8'))

    @classmethod
    def process_data(cls, data):
        """
        processes data
        """
        res = []
        data1 = data.rstrip('\n')
        data_list = data1.split(' ')
        if data_list[0] == 'put':
            if len(data_list) != 4:
                return 'error\nwrong command\n\n'
            try:
                if data_list[1] in cls.storage:
                    cls.storage[data_list[1]].append((data_list[2], data_list[3]))
                else:
                    cls.storage[data_list[1]] = [(data_list[2], data_list[3])]
            except KeyError:
                return 'error\nwrong command\n\n'

        elif data_list[0] == 'get':
            if len(data_list) != 2:
                return 'error\nwrong command\n\n'
            if data_list[1] == '*':
                for key in cls.storage:
                    for i in cls.storage[key]:
                        res_str = ''
                        res_str += key
                        for j in i:
                            res_str += (' ' + j)
                        res.append(res_str)
            else:
                if data_list[1] in cls.storage:
                    for i in cls.storage[data_list[1]]:
                        res_str = ''
                        res_str += data_list[1]
                        for j in i:
                            res_str += (' ' + j)
                        res.append(res_str)
        else:
            return 'error\nwrong command\n\n'

        res.insert(0, 'ok')
        res.append('\n')
        return '\n'.join(res)
