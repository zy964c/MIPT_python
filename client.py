from socket import *
import time

class Client(object):

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.settimeout(timeout)
        self.s.connect((host, port))
        print "connected"

    def put(self, metric, metric_value, timestamp=str(int(time.time()))):
        self.s.send(metric + str(metric_value) + timestamp)
        print "sent"
        data = self.s.recv(10000)
        #if error in answer raise ClientError
        print data
        self.s.close()

    def get(self, metric):
        pass
