import curses
import Views.Menu as Menu
import Views.Login as Login
import Views.Register as Register
import Views.Home as Home
import cliente
import time


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # time out to the user imput
    stdscr.timeout(100)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    currentRow = 0

    # print the menu
    Menu.print_menu(stdscr, currentRow)

    currentView=0

    while 1:
        if(currentView==0):
        #!Menu
            key = stdscr.getch()

            if key == curses.KEY_UP and currentRow > 0:
                currentRow -= 1
            elif key == curses.KEY_DOWN and currentRow < len(Menu.menu)-1:
                currentRow += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                #print_center(stdscr, "You selected '{}'".format(Menu.menu[currentRow]))
                #stdscr.getch()
                if(Menu.menu[currentRow]=='Log in'):
                    currentView=1
                    currentRow=0
                    user=''
                    password=''
                    key=0
                    continue
                elif(Menu.menu[currentRow]=='Register'):
                    currentView=2
                    currentRow=0
                    user=''
                    password=''
                    key=0
                    continue
                # if user selected last row, exit the program
                if currentRow == len(Menu.menu)-1:
                    break

            Menu.print_menu(stdscr, currentRow)


        elif(currentView==1):
            #!Log in
            #mvaddch
            #stdscr.addstr(0, 0,str(key))
            #stdscr.refresh()
            if key == curses.KEY_UP and currentRow > 0:
                currentRow -= 1
            elif key == curses.KEY_DOWN and currentRow < 1:
                currentRow += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                currentView=3
                key=0
                currentRow=0

                jid=user
                xmpp = cliente.Cliente(jid,password)
                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0199') # XMPP Ping
                if xmpp.connect(('redes2020.xyz', 5222)):
                    xmpp.enviarMensaje('dorval@redes2020.xyz','mensaje desde codigo2')
                    xmpp.process(block=False)
                    #time.sleep(20)
                    #xmpp.desconectarse()
                continue

            elif key== 27:
                #? ESC Button
                break
            elif 33<=key<=122:
                if(currentRow==0):
                    user+=chr(key)
                else:
                    password+=chr(key)
            elif key==8:
                if(currentRow==0):
                    user=user[:-1]
                else:
                    password=password[:-1]

            Login.print_menu(stdscr, currentRow,user,password)
            key = stdscr.getch()

        elif(currentView==2):
            #!Register
            #mvaddch
            #stdscr.addstr(0, 0,str(key))
            #stdscr.refresh()
            if key == curses.KEY_UP and currentRow > 0:
                currentRow -= 1
            elif key == curses.KEY_DOWN and currentRow < 1:
                currentRow += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                key=0

                jid=user
                xmpp = cliente.RegisterClient(jid,password)
                xmpp.register_plugin('xep_0030')  # Service Discovery
                xmpp.register_plugin('xep_0004')  # Data forms
                xmpp.register_plugin('xep_0066')  # Out-of-band Data
                xmpp.register_plugin('xep_0077')  # In-band Registration
                xmpp['xep_0077'].force_registration = True
                if xmpp.connect(('redes2020.xyz', 5222)):
                    xmpp.process(block=False)

                currentView=0
                currentRow=0
                user=''
                password=''
                key=0
                continue

            elif key== 27:
                #? ESC Button
                break
            elif 33<=key<=122:
                if(currentRow==0):
                    user+=chr(key)
                else:
                    password+=chr(key)
            elif key==8:
                if(currentRow==0):
                    user=user[:-1]
                else:
                    password=password[:-1]

            Register.print_menu(stdscr, currentRow,user,password)
            key = stdscr.getch()

        elif(currentView==3):
            #!Home
            key = stdscr.getch()
            
            if key == curses.KEY_UP and currentRow > 0:
                currentRow -= 1
            elif key == curses.KEY_DOWN and currentRow < len(Home.menu)-1:
                currentRow += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                #print_center(stdscr, "You selected '{}'".format(Menu.menu[currentRow]))
                #stdscr.getch()
                if(Home.menu[currentRow]=='Log in'):
                    currentView=1
                    currentRow=0
                    user=''
                    password=''
                    key=0
                    continue
                
                # if user selected last row, exit the program
                if currentRow == len(Home.menu)-1:
                    xmpp.desconectarse()
                    break

            Home.print_menu(stdscr, currentRow)



curses.wrapper(main)