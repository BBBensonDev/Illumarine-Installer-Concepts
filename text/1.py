import curses
import sys
import argparse



def main(stdscr):
  curses.curs_set(0)  # Hide cursor
  logo = [
    " Illumarine (insert version here)",
    " Text-Based System Installation Tool "
  ]
  # Assign keybinds to each menu option
  menu = [
    ('Start', 's'),
    ('Settings', 't'),
    ('Exit', 'e')
  ]
  current_row = 0

  while True:
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    total_height = len(logo) + len(menu)
    start_y = h // 2 - total_height // 2

    # Draw logo
    for idx, line in enumerate(logo):
      x = w // 2 - len(line) // 2
      stdscr.addstr(start_y + idx, x, line)

    # Draw menu with keybinds
    for idx, (row, key) in enumerate(menu):
      menu_text = f"[{key.upper()}] {row}"
      x = w // 2 - len(menu_text) // 2
      y = start_y + len(logo) + idx
      if idx == current_row:
        stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(y, x, menu_text)
        stdscr.attroff(curses.A_REVERSE)
      else:
        stdscr.addstr(y, x, menu_text)

    # Screenreader-friendly: print current selection and instructions at the bottom
    info = f"Selected: {menu[current_row][0]}. Press {', '.join([f'{k.upper()} for {n}' for n, k in menu])}."
    stdscr.addstr(h-2, 2, info[:w-4])

    stdscr.refresh()

    key = stdscr.getch()
    if key == curses.KEY_UP and current_row > 0:
      current_row -= 1
    elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
      current_row += 1
    elif key in [ord(menu[0][1]), ord(menu[0][1].upper())]:
      # Start
      current_row = 0
      # Add Start action here
    elif key in [ord(menu[1][1]), ord(menu[1][1].upper())]:
      # Settings
      current_row = 1
      # Add Settings action here
    elif key in [ord(menu[2][1]), ord(menu[2][1].upper())]:
      # Exit
      current_row = 2
      break
    elif key in [curses.KEY_ENTER, ord('\n')]:
      if menu[current_row][0] == 'Exit':
        break
      # Add actions for other menu items here

def main_cli():
  print("Illumarine (insert version here)")
  print("Text-Based System Installation Tool")
  print("This is the CLI mode. Use --menu to launch the curses menu.\n")

  menu = [
    ('Start', 's'),
    ('Settings', 't'),
    ('Exit', 'e')
  ]

  # Print menu options with numbers
  for idx, (name, key) in enumerate(menu, 1):
    print(f"{idx}. {name} [{key.upper()}]")

  while True:
    choice = input("\nSelect an option (1/2/3 or S/T/E): ").strip().lower()
    if choice in ['1', 's']:
      print("You selected Start.")
      # Add Start action here
      break
    elif choice in ['2', 't']:
      print("You selected Settings.")
      # Add Settings action here
      break
    elif choice in ['3', 'e']:
      print("Exiting.")
      break
    else:
      print("Invalid input. Please enter 1, 2, 3, S, T, or E.")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Illumarine Installer")
  parser.add_argument('--menu', action='store_true', help='Launch the curses menu')
  args = parser.parse_args()

  if args.menu:
    curses.wrapper(main)
  else:
    main_cli()