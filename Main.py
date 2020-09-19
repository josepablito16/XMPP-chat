from Cliente import *
import time
'''
jid='tomas@redes2020.xyz'
password='Tomas2020'
'''


jid='jode@redes2020.xyz'
password='Jode2020'

xmpp = Cliente(jid,password)
xmpp.register_plugin('xep_0030') # Service Discovery
xmpp.register_plugin('xep_0199') # XMPP Ping

# Connect to the XMPP server and start processing XMPP stanzas.
if xmpp.connect(('redes2020.xyz', 5222)):


    #xmpp.enviarMensaje('dorval@redes2020.xyz','mensaje desde codigo2')
    xmpp.eliminarCuenta(jid,password)
    xmpp.process(block=False)
    time.sleep(5)
    xmpp.desconectarse()
    print("Done")
else:
    print("Unable to connect.")