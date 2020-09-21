import curses


def print_menu(stdscr, selected_row_idx,user,password):
    menu = ['User: '+str(user), 'Password: '+str('*'*len(password)),'Press ENTER to register']
    stdscr.clear()
    # turn on cursor blinking
    #curses.curs_set(1)
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            #stdscr.move(y, x)
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

