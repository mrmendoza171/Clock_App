
import pyglet
import os

BASE_URL = os.getcwd()
pyglet.font.add_file(os.path.join('assets','fonts',"ds-digital.ttf"))


date_format = "%Y-%m-%dT%H:%M:%SZ"
date_format_print = "%Y-%m-%d %H:%M:%S"
time_format = '%Y-%m-%d %H:%m:%S'

font_name = "Helvetica"


BACKGROUND = 'black'
PRIMARY = '#3a3b3c'
SECONDARY = '#242526'
TERTIARY = '#151617'
TEXT_COLOR = 'white'
BTN_COLOR = '#0029ce'
BTN_TEXT_COLOR = 'white'
NEON_COLOR = '#00ff00'  # neon green
TERMINAL_COLOR = 'black',
ODD_COLOR = '#bdbccf',
EVEN_COLOR = '#a2a0bc'

