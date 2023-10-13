from gpiozero import GPIO
import spidev
from time import sleep

spi = spidev.SpiDev()  #enable spi
CS_Pin = GPIO(23)
data=[0xAA]
data2=[0x11]
spi.open(0,0)#open and initialize the SPI communication with a specific SPI device connected to the SPI bus.
# bus port 0 to establish spi
spi.max_speed_hz = 1000# MAX6675(ADC) is of 4.3MHz 
spi.mode = 0
CS_Pin.off()
result = spi.xref2(data)
result = spi.xref2(data2)
CS_Pin.on()
print("i finished transmitting")