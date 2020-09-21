from Cliente import *
import time
import threading
'''
jid='tomas@redes2020.xyz'
password='Tomas2020'
'''


jid='jirafa@redes2020.xyz'
password='Jirafa2020'

xmpp = Cliente(jid,password)
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0004')
xmpp.register_plugin('xep_0066')
xmpp.register_plugin('xep_0077')
xmpp.register_plugin('xep_0050')
xmpp.register_plugin('xep_0047')
xmpp.register_plugin('xep_0231')
xmpp.register_plugin('xep_0045')
xmpp.register_plugin('xep_0095')  # Offer and accept a file transfer
xmpp.register_plugin('xep_0096')  # Request file transfer intermediate
xmpp.register_plugin('xep_0047')  # Bytestreams

xmpp['xep_0077'].force_registration = True
xmpp.received = set()
xmpp.presences_received = threading.Event()

# Connect to the XMPP server and start processing XMPP stanzas.
if xmpp.connect(('redes2020.xyz', 5222)):


    #xmpp.enviarMensaje('dorval@redes2020.xyz','mensaje desde codigo2')
    #xmpp.eliminarCuenta()
    xmpp.getAllUsers()
    xmpp.process(block=False)
    time.sleep(5)
    xmpp.desconectarse()
    print("Done")
else:
    print("Unable to connect.")