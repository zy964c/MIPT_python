import socket
import time

class ClientError(Exception):
    """
    Custom exception
    """
    pass

class Client(object):
    """
    Client class
    """
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    @staticmethod
    def parse_metric(metric_recieved):
        """
        parses data recieved
        """
        dict1 = {}
        metric = metric_recieved.decode("utf8")
        if metric == "error\nwrong command\n\n":
            raise ClientError
        #print(metric)
        list_metric = metric.split('\n')
        #print(list_metric)
        if len(list_metric) < 4:
            return dict1
        data = list_metric[1:-2]
        #print(data)
        for i in data:
            list_data = i.split()
            metric_name = list_data[0]
            metric_val = float(list_data[1])
            timestamp = int(list_data[2])
            if metric_name in dict1:
                dict1[metric_name].append(tuple([timestamp, metric_val]))
            else:
                dict1[metric_name] = [tuple([timestamp, metric_val])]
        for j in dict1:
            dict1[j].sort(key=lambda tup: tup[0])
        return dict1

    def put(self, metric, m_value, timestamp=str(int(time.time()))):
        """
        Put data on the server
        """
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                #sock.settimeout(self.timeout)
                data_to_sent = 'put {0} {1} {2}\n'.format(metric, m_value, timestamp)
                bytes_sent = sock.sendall(data_to_sent.encode(encoding='utf_8'))
                data = sock.recv(10000)
            except:
                raise ClientError
            #print 'sent {0} bytes of data'.format(bytes_sent)
            #print data

    def get(self, metric):
        """
        gets data from the server
        """
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                #sock.settimeout(self.timeout)
                data_to_sent = 'get {0}\n'.format(metric)
                sock.sendall(data_to_sent.encode(encoding='utf_8'))
                data = sock.recv(10000)
            except:
                raise ClientError
            res = Client.parse_metric(data)
            return res
