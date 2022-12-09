try:
  import usocket as socket
except:
  import socket

import network # allow us to connet esp32 or esp8266 to a wifi network

import esp      
esp.osdebug(None)     # garbage collector

from machine import Pin

import gc
gc.collect()

ssid = 'Sarada school'    
password = 'ssvn2021'

station = network.WLAN(network.STA_IF)    # WiFi station

station.active(True)
station.connect(ssid, password)     # connect out esp board to our router

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())
def web_page():
    html = """<html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body>
    <style>
.button {
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50;
}

.button1:hover {
  background-color: #4CAF50;
  color: white;
}

.button2 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button2:hover {
  background-color: #008CBA;
  color: white;
}
header {
  background-color: #ff1a1a;
  padding: 20px;
  text-align: center;
  font-size: 25px;
  color: white;
}
</style>
<header>
    <h1>Smart Farming</h1>
</header>
    <h2>Motor control</h2>
    <a href=\"?led=off\"><button class="button button1">ON</button></a>&nbsp;
    <a href=\"?led=on\"><button class="button button2">OFF</button></a>
    </body>
    </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
led = Pin(16,Pin.OUT)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6:
        print('LED ON\n')
        print(led_on)
        led.value(1)
    if led_off == 6:
        print('LED OFF\n')
        print(led_off)
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
