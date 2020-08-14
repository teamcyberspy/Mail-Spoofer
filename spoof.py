from modules import send

_ = lambda x: str(input(x))

class Spoof:
	def __init__(self):
		send.check()
		self.menu()

	def menu(self):
		em = _("[*] Sender Email: ")
		nm = _("[*] Sender Name : ")
		to = _("[*] Email Target: ")
		sb = _("[*] Subject     : ")
		ms = _("[*] Your Message: ")
		try:
			__ = send.send(em, nm, to, sb, ms)
			if __ == True:
				print ("[*] Success sended")
			else:
				print ("[!] Email not sended")
		except:
			exit("[!] Error detected")

Spoof()
