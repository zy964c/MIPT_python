from socket import *
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
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.settimeout(timeout)
        #self.s.connect((host, port))
        #print ("connected")

    @staticmethod
    def parse_metric(metric):
        """
        parses data recieved
        """
        dict1 = {}
        list_metric = metric.split('\\')
        if len(list_metric) < 4:
            return dict1
        data = list_metric[1:-2]
        #print data
        for i in data:
            list_data = i.split()
            metric_name = list_data[0]
            metric_val = float(list_data[1])
            timestamp = int(list_data[2])
            if metric_name in dict1:
                dict1[metric_name].append(tuple(timestamp, metric_val))
            else:
                dict1[metric_name] = [tuple(timestamp, metric_val)]
        for j in dict1:
            dict1[j].sort(key=lambda tup: tup[0])
        return dict1

    def put(self, metric, m_value, timestamp=str(int(time.time()))):
        """
        Put data on the server
        """
        self.s.connect((self.host, self.port))
        try:
            bytes_sent = self.s.send(bytearray('put {0} {1} {2}\n'.format(metric, m_value, timestamp)))
            data = self.s.recv(10000)
        except:
            self.s.close()
            raise ClientError
        if data != 'ok\n\n':
            self.s.close()
            raise ClientError
        #print 'sent {0} bytes of data'.format(bytes_sent)
        #print data
        self.s.close()

    def get(self, metric):
        """
        gets data from the server
        """
        self.s.connect((self.host, self.port))
        try:
            self.s.send(bytearray('get {0}\n'.format(metric)))
            data = self.s.recv(10000)
        except:
            self.s.close()
            raise ClientError
        res = Client.parse_metric(data)
        self.s.close()
        return res
