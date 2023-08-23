from enum import Enum
from .transport import Transport, TcpTransport

class GqrxClientError:
    pass

class CommandFailedGqrxClientError(GqrxClientError):
    pass

class DemodulatorMode(Enum):
    OFF = 'OFF'
    RAW = 'RAW'
    AM = 'AM'
    AMS = 'AMS'
    LSB = 'LSB'
    USB = 'USB'
    CWL = 'CWL'
    CWR = 'CWR'
    CWU = 'CWU'
    CW = 'CW'
    FM = 'FM'
    WFM = 'WFM'
    WFM_ST = 'WFM_ST'
    WFM_ST_OIRT = 'WFM_ST_OIRT'

class GqrxClient:

    def __init__(self):
        self.transport: Transport = None

    def open(self, addr = ('127.0.0.1', 7356)):
        self.transport = TcpTransport()
        self.transport.open(addr)
    
    def _do(self, command):
        self.transport.send(bytes(command, 'ascii'))
        return self.transport.recv().decode('ascii')

    def _check_ok(self, response):
        if response != 'RPRT 0':
            raise CommandFailedGqrxClientError()

    @property
    def frequency(self):
        response = self._do('f')
        return int(response)

    @frequency.setter
    def frequency(self, value: int):
        response = self._do(f'F {value}')
        self._check_ok(response)
    
    @property
    def demodulator(self):
        self.transport.send(bytes('m', 'ascii'))
        mode = self.transport.recv().decode('ascii')
        passband = self.transport.recv().decode('ascii')
        return (DemodulatorMode[mode], int(passband))

    @demodulator.setter
    def demodulator(self, value: DemodulatorMode | str | tuple[DemodulatorMode | str, int | None]):

        # If the value is not a tuple, make it one
        if not isinstance(value, tuple):
            value = (value, None)

        # Extract the mode and passband
        (mode, passband) = value

        # If the mode is an enum instance, get the value
        if isinstance(mode, DemodulatorMode):
            mode = mode.value

        # If no passband is set, only send the mode
        if passband is None:
            response = self._do(f'M {mode}')
        
        # Otherwise, send the mode and passband
        else:
            response = self._do(f'M {mode} {passband}')
        
        # Make sure things don't break
        self._check_ok(response)

    @property
    def dsp(self):
        response = self._do('u DSP')
        return bool(int(response))
    
    @dsp.setter
    def dsp(self, value: bool):
        response = self._do(f'U DSP {int(value)}')
        self._check_ok(response)

    @property
    def recording(self):
        response = self._do('u RECORD')
        return bool(int(response))

    @recording.setter
    def recording(self, value: bool):
        response = self._do(f'U RECORD {int(value)}')
        self._check_ok(response)
    
    def aos(self):
        response = self._do(f'AOS')
        self._check_ok(response)
    
    def los(self):
        response = self._do(f'LOS')
        self._check_ok(response)
    
