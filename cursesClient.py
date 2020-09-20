import curses
import Views.Menu as Menu
import Views.Login as Login
from Cliente import *
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
                currentView=2
                key=0

                jid=user
                xmpp = Cliente(jid,password)
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
            if key== 27:
                #? ESC Button
                xmpp.desconectarse()
                break
            stdscr.addstr(0, 0,str(xmpp.getMensajePrueba()))
            stdscr.refresh()
            key = stdscr.getch()



curses.wrapper(main)