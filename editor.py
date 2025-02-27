import curses


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    menu = ["Option 1", "Option 2", "Option 3", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()
        for idx, item in enumerate(menu):
            mode = curses.A_REVERSE if idx == current_row else curses.A_NORMAL
            stdscr.addstr(idx + 1, 1, item, mode)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord("\n"):  # Enter key
            if menu[current_row] == "Exit":
                break

        stdscr.refresh()


curses.wrapper(main)
