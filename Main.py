import time
import cliente
import sys
import os

moveUp=lambda n:u"\u001b["+str(n)+"A"

cleanLine=lambda :u"\u001b["+str(2)+"K"

# Hanldes the client once the user logged in
def handle_session(event):
    xmpp.start()
    #xmpp.enviarMensaje('dorval@redes2020.xyz','Dorval2020')
    #xmpp.getAllUsers()
    #xmpp.getMyContacts()
    #xmpp.addSubscription('tomas@redes2020.xyz')
    #xmpp.getContact('dorval2@redes2020.xyz')
    print(cliente.inbox)
    xmpp.updateInboxContacts()
    print(cliente.inbox)
    print(xmpp.getListOfContact())
    '''
    os.system('cls')
    cliente.inbox['dorval@redes2020.xyz'].printChat()
    while 1:
        userInput=input('> ')
        sys.stdout.write(moveUp(1))
        sys.stdout.write(cleanLine())
        sys.stdout.flush()
        if(userInput=='exit()'):
            break
        if(userInput!=''):
            xmpp.enviarMensaje('josepa@redes2020.xyz',userInput)
            cliente.inbox['dorval@redes2020.xyz'].newMessage('Jose',userInput)
        

        cliente.inbox['dorval@redes2020.xyz'].printUntracked()

    #xmpp.deleteAccount()
    '''
    xmpp.desconectarse()



if __name__ == "__main__":

    username = 'tomas@redes2020.xyz'
    password = 'Tomas2020'

    #username = 'dorval@redes2020.xyz'
    #password = 'Dorval2020'
    #username ='jirafa@redes2020.xyz'
    #password ='Jirafa2020'
    xmpp = cliente.Cliente(username, password)

    xmpp.add_event_handler("session_start", handle_session, threaded=True)
    if xmpp.connect(('redes2020.xyz', 5222)):
        xmpp.process(block=False)
        #time.sleep(5)
    else:
        xmpp.desconectarse()
