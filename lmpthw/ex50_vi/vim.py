import os, sys
import curses


# simple curses screen
# have the gutter commands for ed change the file display
# do a cleaner display method


def draw_window(stdscr):
    key = 0
    cursor_x = 0
    cursor_y = 0

    # clear and refresh the screen
    stdscr.clear()
    stdscr.refresh()

    # start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_MAGENTA)

    # get the size of the terminal

    # status bar text
    statusbarstr = f"Press 'q' to exit | Pos: {cursor_x}, {cursor_y}3"

    # last clicked key
    while (key != ord('q')):
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if key == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif key == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif key == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif key == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # render status bar
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(1))

        # refresh the screen
        stdscr.refresh()

        # wait for next input
        key = stdscr.getch()

def main():
    curses.wrapper(draw_window)

if __name__ == "__main__":
    main()


