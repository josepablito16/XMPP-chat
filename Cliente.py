'''
	Author: Jose Cifuentes
	This script contains all related
	to de xmpp client, for example, chat class,
	message class and client class
'''
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from xml.etree import cElementTree as ET
from sleekxmpp.plugins.xep_0004.stanza.field import FormField, FieldOption
from sleekxmpp.plugins.xep_0004.stanza.form import Form
from sleekxmpp.plugins.xep_0047.stream import IBBytestream

'''
	Structure that saves all
	the chats:
		User: [Messages]
'''
inbox={}
class Chat(object):
	""" Saves all the messages of a conversation"""
	def __init__(self):
		self.chat=[] # All the chat
		self.untracked=[] # The messages that not are printed

	# Add a new message to the array
	# user: the user that send the message
	# message: the message sended
	def newMessage(self,user,message):
		self.chat.append(Message(user,message))
		self.untracked.append(Message(user,message))

	# Prints all the message untracked and clean the untracked array
	def printUntracked(self):
		for i in self.untracked:
			print(i.getMensaje())
		self.untracked=[]

	# returns if the chat is untracked
	def isUntracked(self):
		return len(self.untracked)!=0

	# prints all the chat and clean the untracked array
	def printChat(self):
		self.untracked=[]
		for i in self.chat:
			print(i.getMensaje())

	# print the last message
	def printLastMessage(self):
		print(self.chat[-1].getMensaje())


class Message(object):
	def __init__(self,user,message):
		self.user=user # user that send the message
		self.message=message 

	# return the message to print, for example,
	#	Jose: Hello!
	def getMensaje(self):
		return self.user+": "+self.message




class Cliente(ClientXMPP):
	""""All the interaction to the xmpp server"""
	def __init__(self, jid, password):

		ClientXMPP.__init__(self, jid, password)
		# authorize automatically subscriptions
		self.auto_authorize = True
		self.auto_subscribe = True

		# Array that saves all the notifications, for example
		# new messages, when a user got online, etc
		self.notifications=[]

		self.add_event_handler("message", self.mensajeNuevo) # event that handle when receive a new message
		self.add_event_handler("got_online", self.gotOnline) # event that handle when a user got online
		self.add_event_handler("got_offline", self.gotOffline) # event that handle when a user got off line
		self.add_event_handler('changed_status', self.changedStatus) # event that handle when a user change his status
		

		self.register_plugin('xep_0030') # Service Discovery
		self.register_plugin('xep_0004') # Data Forms
		self.register_plugin('xep_0066')
		self.register_plugin('xep_0077') # In-Band Registration
		self.register_plugin('xep_0050')
		self.register_plugin('xep_0047')
		self.register_plugin('xep_0231')
		self.register_plugin('xep_0045') # Multi-User Chat

		self['xep_0077'].force_registration = True
	
	def mensajeNuevo(self,msg):
		userFrom=str(msg['from'])
		inbox[userFrom[:userFrom.find('/')]].newMessage(userFrom[:userFrom.find('@')],str(msg['body']))
		self.notifications.append('message from '+userFrom[:userFrom.find('@')])
	
	# Add to notification array when a user chage the status
	# msg is the data thtat provides the server
	def changedStatus(self,msg):
		statusDict={
        "":'available',
        'away':'away',
        'dnd':'Busy',
        'xa':'Not available'}
		user=str(msg['from'])
		newStatus=str(msg['show'])
		if(user!=self.boundjid.full):
			self.notifications.append(user[:user.find('@')]+' is '+statusDict[newStatus])
	
	# Add to notification array when a user got off line
	# msg is the data thtat provides the server
	def gotOffline(self,msg):
		user=str(msg['from'])
		if(user!=self.boundjid.full):
			self.notifications.append(user[:user.find('@')]+' is offline')

	# Add to notification array when a user got online
	# msg is the data thtat provides the server
	def gotOnline(self,msg):
		user=str(msg['from'])
		if(user!=self.boundjid.full):
			self.notifications.append(user[:user.find('@')]+' is online')
	
	# Update the inbox structure
	def updateInbox(self,user):
		if(user not in inbox):
			inbox[user]=Chat()
	
	# Send the presence message and status to the server
	def SendPresenceMessage(self,newPresence,newStatus):
		self.send_presence(pshow=newPresence, pstatus=newStatus)

	def updateInboxContacts(self):
		try:
			self.get_roster(block=True)
		except IqError as err:
			print('Error: %s' % err.iq['error']['condition'])
		except IqTimeout:
			print('Error: Request timed out')

		clientGroups = self.client_roster.groups()
		for group in clientGroups:
			for user in clientGroups[group]:
				
				# exclude the actual account
				if user == self.boundjid.bare:
					continue

				subscription = self.client_roster[user]['subscription']
				connections = self.client_roster.presence(user)

				# Get all users connected
				if connections.items():
					for platform, status in connections.items():
						self.updateInbox(user)
 

				# Get all users offline
				else:
					self.updateInbox(user)
	
	# return all the contacts in a list
	def getListOfContact(self):
		contactList=[]
		try:
			self.get_roster(block=True)
		except IqError as err:
			print('Error: %s' % err.iq['error']['condition'])
		except IqTimeout:
			print('Error: Request timed out')

		clientGroups = self.client_roster.groups()
		for group in clientGroups:
			for user in clientGroups[group]:
				
				# exclude the actual account
				if user == self.boundjid.bare:
					continue

				subscription = self.client_roster[user]['subscription']
				connections = self.client_roster.presence(user)

				# Get all users connected
				if connections.items():
					for platform, status in connections.items():	
						contactList.append([user,inbox[user].isUntracked()])
						

				# Get all users offline
				else:
					contactList.append([user,inbox[user].isUntracked()])
				
		return contactList

	# print the info of a user
	def getContact(self,userSearch):
		try:
			self.get_roster(block=True)
		except IqError as err:
			print('Error: %s' % err.iq['error']['condition'])
		except IqTimeout:
			print('Error: Request timed out')

		clientGroups = self.client_roster.groups()
		for group in clientGroups:
			for user in clientGroups[group]:
				
				# exclude the actual account
				if user == self.boundjid.bare:
					continue

				subscription = self.client_roster[user]['subscription']
				connections = self.client_roster.presence(user)

				# Get all users connected
				if connections.items():
					for platform, status in connections.items():
						
						if status['show']:
							if(status['show']=='dnd'):
								status='busy'
							elif(status['show']=='xa'):
								status='Not available'
							else:
								status = status['show']
						else:
							status = 'available'

						if(userSearch==user):
							print()
							print(user)
							print('\t- Status: '+str(status))
							print('\t- Subscription: '+str(subscription))
							print('\t- Platform: '+str(platform))
							return 

				# Get all users offline
				else:
					if(userSearch==user):
						print()
						print(user)
						print('\t- Status: unavailable')
						print('\t- Subscription: '+str(subscription))
						break
		print('User not found!')
	
	# prints all the contacts
	def getMyContacts(self):
		try:
			self.get_roster(block=True)
		except IqError as err:
			print('Error: %s' % err.iq['error']['condition'])
		except IqTimeout:
			print('Error: Request timed out')

		clientGroups = self.client_roster.groups()
		for group in clientGroups:
			for user in clientGroups[group]:
				
				# exclude the actual account
				if user == self.boundjid.bare:
					continue

				subscription = self.client_roster[user]['subscription']
				connections = self.client_roster.presence(user)

				# Get all users connected
				if connections.items():
					for platform, status in connections.items():
						
						if status['show']:
							if(status['show']=='dnd'):
								status='busy'
							elif(status['show']=='xa'):
								status='Not available'
							else:
								status = status['show']
						else:
							status = 'available'

						print()
						print(user)
						print('\t- Status: '+str(status))
						print('\t- Subscription: '+str(subscription))
						print('\t- Platform: '+str(platform))

				# Get all users offline
				else:
					print()
					print(user)
					print('\t- Status: unavailable')
					print('\t- Subscription: '+str(subscription))
	
	# prints all the user of the server
	def getAllUsers(self):
		# New form to the response
		formResponse = Form()
		formResponse.set_type('submit')

		formResponse.add_field(
			var='FORM_TYPE',
			ftype='hidden',
			type='hidden',
			value='jabber:iq:search'
		)

		formResponse.add_field(
			var='search',
			ftype='text-single',
			type='text-single',
			label='Search',
			required=True,
			value='*'
		)

		#Only define the username
		formResponse.add_field(
			var='Username',
			ftype='boolean',
			type='boolean',
			label='Username',
			value=1
		)
		# Create a iq to search using the form created
		search = self.Iq()
		search.set_type('set')
		search.set_to('search.'+self.boundjid.domain)
		search.set_from(self.boundjid.full)

		newQuery = ET.Element('{jabber:iq:search}query')
		newQuery.append(formResponse.xml)
		search.append(newQuery)
		results = search.send(now=True, block=True)

		# Convert the string result to structure
		results = ET.fromstring(str(results))
		ResultItems = []

		#Iterate the structure to get all the items
		for child in results:
			for node in child:
				for item in node:
					ResultItems.append(item)

		usersNames=[]
		# iterate the result items
		for item in ResultItems:
			for field in item.getchildren():
				try:
					if(field.attrib['var']=='Username'):
						usersNames.append(field.getchildren()[0].text)
				except:
					continue

		# order alphabetically all the user names
		sortedUserNames=sorted(usersNames, key=str.lower)
		for i in range(len(sortedUserNames)) :
			print(f'{i+1}. {sortedUserNames[i]}')

	def deleteAccount(self):
		resp = self.Iq()
		resp['type'] = 'set'
		resp['from'] = self.boundjid.full
		resp['register']['remove'] = True

		try:
			resp.send(now=True)
		except IqError as e:
			print('Could not unregister account: %s' %
						  e.iq['error']['text'])
			self.disconnect()
		except IqTimeout:
			print('No response from server.')
			self.disconnect()
	
	# send message
	def enviarMensaje(self,contacto,mensaje):
		self.sendMessage(mto=contacto,
						  mbody=mensaje,
						  mtype='chat')
	
	# disconect to the server
	def desconectarse(self):
		# Using wait=True ensures that the send queue will be
		# emptied before ending the session.
		self.disconnect()

	def start(self):
		self.send_presence()
		self.get_roster()
		self.updateInboxContacts()

class RegisterClient(ClientXMPP):

	def __init__(self, jid, password):
		ClientXMPP.__init__(self, jid, password)

		# The session_start event will be triggered when
		# the bot establishes its connection with the server
		# and the XML streams are ready for use. We want to
		# listen for this event so that we we can initialize
		# our roster.
		self.add_event_handler("session_start", self.start, threaded=True)

		# The register event provides an Iq result stanza with
		# a registration form from the server. This may include
		# the basic registration fields, a data form, an
		# out-of-band URL, or any combination. For more advanced
		# cases, you will need to examine the fields provided
		# and respond accordingly. SleekXMPP provides plugins
		# for data forms and OOB links that will make that easier.
		self.add_event_handler("register", self.register, threaded=True)

	def start(self, event):
		self.send_presence()
		self.get_roster()

		# We're only concerned about registering, so nothing more to do here.
		self.disconnect()

	def register(self, iq):
		resp = self.Iq()
		resp['type'] = 'set'
		resp['register']['username'] = self.boundjid.user
		resp['register']['password'] = self.password

		try:
			resp.send(now=True)
			print("Account created for %s!" % self.boundjid)
		except IqError as e:
			print("Could not register account: %s" %
						  e.iq['error']['text'])
			self.disconnect()
		except IqTimeout:
			print("No response from server.")
			self.disconnect()