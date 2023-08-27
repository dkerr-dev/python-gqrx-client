import logging
import time
from gqrx_client import GqrxClient, DemodulatorMode

def main():
    client = GqrxClient()
    client.open()

    print(client.frequency)

    client.demodulator = DemodulatorMode.RAW, 38000
    print(client.demodulator)

    client.demodulator = DemodulatorMode.WFM, 36000
    print(client.demodulator)

    # client.dsp = True
    # client.recording = True
    # time.sleep(1.0)
    # client.recording = not client.recording

    # time.sleep(1.0)
    # client.aos()
    # time.sleep(2.0)
    # client.los()

    # time.sleep(2.0)
    # client.dsp = False

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
