import time
import cliente

# Hanldes the client once the user logged in
def handle_session(event):
    xmpp.start()
    xmpp.enviarMensaje('dorval@redes2020.xyz','Dorval2020')



if __name__ == "__main__":

    username = 'jirafa@redes2020.xyz'
    password = 'Jirafa2020'

    xmpp = cliente.Cliente(username, password)

    xmpp.add_event_handler("session_start", handle_session, threaded=True)
    if xmpp.connect(('redes2020.xyz', 5222)):
        xmpp.process(block=False)
        time.sleep(5)
        xmpp.desconectarse()
    else:
        xmpp.desconectarse()
