from bluepy import btle

DEFAULT_DEVICE_ID = ""


class DoorDevice(object):
    def __init__(self, device_id=DEFAULT_DEVICE_ID):
        self.device_id = device_id
        self.connected = False
        self._connect()

    def _connect(self):
        if self.connected:
            return

        try:
            print("Connecting...")
            self.device = btle.Peripheral(self.device_id)
            self.connected = True
        except BTLEException as e:
            print("DoorDevice failed to connect")
            print(e)
            raise

    def _disconnect(self):
        if self.connected:
            self.device.disconnect()
        self.connected = False
