import curses
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.nodelay(True)  # Don't block for input
    curses.curs_set(0)  # Hide cursor

    stdscr.addstr(0, 0, "Control the rover: Arrow keys (FWD, LEFT, RIGHT), 'r' (reverse), Space (stop), 'q' (quit)")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            stdscr.addstr(2, 0, "Moving forward  ")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(2, 0, "Moving backward ")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(2, 0, "Turning left   ")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(2, 0, "Turning right  ")
        elif key == ord('r'):
            stdscr.addstr(2, 0, "Reversing       ")
        elif key == ord(' '):
            stdscr.addstr(2, 0, "Stopped         ")
        elif key == ord('q'):
            break  # Quit the loop

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
