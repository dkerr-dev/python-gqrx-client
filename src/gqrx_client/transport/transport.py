import logging

class Transport:

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def send(self, message: bytes) -> None:
        raise NotImplementedError()

    def recv(self) -> bytes:
        raise NotImplementedError()
