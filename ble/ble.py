from bluepy import btle

DEFAULT_DEVICE_ID = "e9:99:e8:f2:55:4d"
TX_CHAR_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

class DoorDevice(object):

    OPEN_CMD = b"\x00\x00\x01"
    CLOSE_CMD = b"\x00\x00\x00"

    def __init__(self, device_id=DEFAULT_DEVICE_ID):
        self.device_id = device_id
        self.device = None
        self.tx_char = None
        self.connected = False
        self._connect()

    def _connect(self):
        try:
            print("Connecting...")
            self.device = btle.Peripheral(self.device_id, addrType="random")

            self.tx_char = self.device.getCharacteristics(uuid=TX_CHAR_UUID)[0]

            self.connected = True
        except btle.BTLEException as e:
            print("DoorDevice failed to connect: {}".format(e))
            raise

    def _disconnect(self):
        if self.connected:
            self.device.disconnect()
            self.device = None
        self.connected = False

    def _send_cmd(self, cmd):
        if self.connected:
            # validation logic for sending command to go here
            self.tx_char.write(cmd)

    def openDoor(self):
        self._send_cmd(self.OPEN_CMD)

    def closeDoor(self):
        self._send_cmd(self.CLOSE_CMD)
