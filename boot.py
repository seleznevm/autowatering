# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

ssid = 'IPC_Zy_Openspace_24' # IPC_Zy_Openspace_24
password = 'ipc2320207'
mqtt_server = 'test.mosquitto.org' # 5.196.95.208
client_id = 'NodeMCU_SMA2020'


