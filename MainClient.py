import time
import cliente
import Menus
import os
import sys
import platform
from inputimeout import inputimeout, TimeoutOccurred

moveUp=lambda n:u"\u001b["+str(n)+"A"

cleanLine=lambda :u"\u001b["+str(2)+"K"

# Hanldes the client once the user logged in
def handle_session(event):
	xmpp.start()
	while 1:
		os.system(BORRAR)
		try:
			Menus.printHomeMenu()
			userInput = inputimeout(prompt='>>', timeout=5)
			if(Menus.validarInputHome(userInput)):
				print('sin errores')
				time.sleep(1)
				if(userInput=='1'):
					#? show all users
					os.system(BORRAR)
					Menus.printAllusersMenu()
					xmpp.getAllUsers()
					input('\nPress Enter to continue...')
					os.system(BORRAR)

					Menus.printMyusersMenu()
					xmpp.getMyContacts()
					input('\nPress Enter to continue...')
				elif(userInput=='2'):
					#? Subscribe to user
					os.system(BORRAR)
					user=Menus.printAddUserMenu()
					xmpp.addSubscription(user)
				elif(userInput=='3'):
					#? search contact
					os.system(BORRAR)
					user=Menus.printSearchContact()
					xmpp.getContact(user)
					input('\nPress Enter to continue...')
				elif(userInput=='4'):
					#? Inbox
					os.system(BORRAR)
					userInput,control=Menus.printInboxMenu(xmpp.getListOfContact())
					if(userInput!=-100):
						print(userInput)
						if(control):
							xmpp.updateInbox(userInput)
						os.system(BORRAR)
						xmpp.updateInboxContacts()
						
						Menus.printMenuChat(userInput)
						cliente.inbox[userInput].printChat()
						while 1:
							try:
								chatInput=inputimeout(prompt='> ', timeout=10)
							except TimeoutOccurred:
								chatInput=""

							sys.stdout.write(moveUp(1))
							sys.stdout.write(cleanLine())
							sys.stdout.flush()
							if(chatInput=='exit()'):
								break
							if(chatInput!=''):
								xmpp.enviarMensaje(userInput,chatInput)
								cliente.inbox[userInput].newMessage('Me',chatInput)
							

							cliente.inbox[userInput].printUntracked()

				elif(userInput=='40'):
					#? Delete account
					xmpp.deleteAccount()
					print('Account deleted!')
					time.sleep(1)
					break
				elif(userInput=='69'):
					break
		except TimeoutOccurred:
			continue
		
	#xmpp.enviarMensaje('dorval@redes2020.xyz','Dorval2020')
	xmpp.desconectarse()
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
				os.system(BORRAR)
				print('Log in')
				#user,password=Menus.printMenuLogIn()
				user,password='tomas@redes2020.xyz','Tomas2020'
				#user,password='jode2@redes2020.xyz','Jode2020'
				xmpp = cliente.Cliente(user,password)
				xmpp.add_event_handler("session_start",handle_session, threaded=True)
				if xmpp.connect(('redes2020.xyz', 5222)):
					xmpp.process(block=False)
					break
			elif(userInput=='2'):
				#!Register
				os.system(BORRAR)
				print('Register')
				user,password=Menus.printMenuRegister()
				xmpp = cliente.RegisterClient(user,password)
				xmpp.register_plugin('xep_0030')  # Service Discovery
				xmpp.register_plugin('xep_0004')  # Data forms
				xmpp.register_plugin('xep_0066')  # Out-of-band Data
				xmpp.register_plugin('xep_0077')  # In-band Registration
				xmpp['xep_0077'].force_registration = True
				if xmpp.connect(('redes2020.xyz', 5222)):
					xmpp.process(block=False)
				print('Account registered successfully!')
				time.sleep(2)
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
