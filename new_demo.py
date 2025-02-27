import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5,10, "Hello world!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
