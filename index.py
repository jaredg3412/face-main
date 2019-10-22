import ble 
import time

dev = ble.DoorDevice()
dev.openDoor()

time.sleep(2)

dev.closeDoor()

input("Press Enter to continue...")

