import usb.core
import sys


class TrafficController:

	def __init__(self):
		self.dev = usb.core.find(idVendor=0x3eb, idProduct=0x204f)
		self.endpoint = None
		if self.dev is not None:
			if self.dev.bcdDevice != 4918:
				print "found device but its not the right serial"

			if self.dev.is_kernel_driver_active(0):
				try:
					self.dev.detach_kernel_driver(0)
					self.dev.set_configuration()
				except:
					print "Warning! Could not detach kernel driver or set config"
			self.endpoint = self.dev[0][(0,0)][0]

	def setLights(self,r=False,a=False,g=False):
		if self.endpoint is not None:
			self.dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09, data_or_wLength=[int(r),int(a),int(g),0,0,0,0,0])
		else:
			print "setting lights with no valid endpoint"



