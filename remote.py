import curses, pycurl
from urllib import urlencode

stdscr = curses.initscr()
stdscr.keypad(1)

roku_ip = '10.0.1.9'
roku_port = '8060'
roku_url = roku_ip + ':' + roku_port

key = ''

post_data = {}
post_fields = urlencode(post_data)

def send_command(command):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, roku_url + '/keypress/' + command)
    c.setopt(pycurl.POSTFIELDS, post_fields)
    c.perform()
    c.close()

while key != ord('q'):
    key = stdscr.getch()

    if key == curses.KEY_UP:
        send_command('up')
    elif key == curses.KEY_DOWN:
        send_command('down')
    elif key == curses.KEY_LEFT:
        send_command('left')
    elif key == curses.KEY_RIGHT:
        send_command('right')
    elif key == curses.KEY_ENTER:
        send_command('select')
    elif key == curses.KEY_HOME:
        send_command('home')

curses.endwin()
