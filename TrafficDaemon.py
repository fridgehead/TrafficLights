from TrafficLight import TrafficController
import socket


tl = TrafficController()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("172.31.24.101", 9009))
while(1):
	msg = sock.recv(100)
	msg = msg.split("\r\n")
	for m in msg:
		m = m.strip()
		if len(m) == 3:
			r = m[0] == '1'
			a = m[1] == '1'
			g = m[2] == '1'
			tl.setLights( r, a, g)

