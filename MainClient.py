import time
import cliente
import Menus
import os
import platform

# Hanldes the client once the user logged in
def handle_session(event):
	print(xmpp)
	xmpp.start()
	xmpp.enviarMensaje('dorval@redes2020.xyz','Dorval2020')
	#xmpp.deleteAccount()



if __name__ == "__main__":
	if(platform.system()=='Windows'):
		BORRAR='cls'
	else:
		BORRAR='clear'

	while True:
		# Clear the screen.
		os.system(BORRAR)
		Menus.printMenuInicial()
		userInput=input('>>')
		print(userInput)
		if(Menus.validarInputMenuInicial(userInput)):
			# No hay errores
			if(userInput=='1'):
				#!Log in
				print('Log in')
			elif(userInput=='2'):
				#!Register
				os.system(BORRAR)
				print('Register')
				Menus.printMenuRegister()
			elif(userInput=='3'):
				#!Exit
				print('Exit')
				break
		print('Que pasa')
			
	'''
	username = 'tomas@redes2020.xyz'
	password = 'Tomas2020'

	xmpp = cliente.Cliente(username, password)

	xmpp.add_event_handler("session_start", handle_session, threaded=True)
	if xmpp.connect(('redes2020.xyz', 5222)):
		xmpp.process(block=False)
		time.sleep(5)
		xmpp.desconectarse()
	else:
		xmpp.desconectarse()
	'''
