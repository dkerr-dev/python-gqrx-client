import socket
from io import BytesIO

from .transport import Transport

class ConnectionClosedError(ConnectionError):
    pass

class TcpTransport(Transport):

    def __init__(self):
        super().__init__()
        self.client: socket.socket = None
        
    """
    Connect to a TCP server.
    @param addr a (host, port) address tuple.
    """
    def open(self, addr = ('127.0.0.1', 7356)):
        self.log.info(f'Establishing TCP connection to {addr}')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(True)
        self.client.connect(addr)
        self.log.info('Connection established')
    
    def close(self):
        self.log.info('Closing connection')
        self.client.close()
        self.client = None
        self.log.info('Connection closed')
        
    def send(self, message: bytes) -> None:
        payload = message + b'\n'
        self.log.debug(f'Sending bytes: {payload}')
        self.client.sendall(payload)
        self.log.debug(f'Sent bytes')
    
    def recv(self) -> bytes:
        self.log.debug(f'Receiving bytes')
        buffer = BytesIO()
        while True:
            c = self.client.recv(1)
            self.log.debug(f'Received byte: {c}')
            if c == b'':
                raise ConnectionClosedError()
            if c == b'\n':
                break
            buffer.write(c)
        buffer.seek(0)
        result = buffer.read()
        self.log.debug(f'Received bytes: {result}')
        return result
