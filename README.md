# Gqrx SDR Client

This is a small client library which allows you to interface with and remotely control a running instance of the [Gqrx SDR](https://gqrx.dk/) application.



# Usage

```python
# Import the Gqrx Client and some other relevant classes
from gqrx_client import GqrxClient, DemodulatorMode, GqrxClientError

# Create a Gqrx Client instance and open the connection
client = GqrxClient()
client.open(addr=('127.0.0.1', 7356))

# Set and then retrieve the current frequency
client.frequency = 137912500
print(f"The current frequency is: {client.frequency}")

# Get the current demodulator mode + passband width values
(mode, passband) = client.demodulator

# Turn on the digital signal processing and start recording
client.dsp = True
client.recording = True
```


# Documentation

[View the documentation here](./docs/_build/html/index.html).
