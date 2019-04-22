import I2C_LCD_driver
import fcntl
import struct

from time import *

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string(get_ip_address('lo', 2, 3)
