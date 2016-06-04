#!/usr/bin/env python

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appind
import subprocess
import signal
import os

APPINDICATOR_ID = 'screen_rotator'

def build_menu():
    menu = Gtk.Menu()
    item_rotleft = Gtk.RadioMenuItem(label='Reading Mode')
    item_rotleft.set_name("readitem")
    item_rotnorm = Gtk.RadioMenuItem(group=item_rotleft, label='Laptop Mode')
    item_rotnorm.set_name("lapitem")

    item_rotleft.connect('activate', rotleft)
    item_rotnorm.connect('activate', rotnorm)

    item_rotleft.set_draw_as_radio(True)
    item_rotnorm.set_draw_as_radio(True)

    item_rotnorm.set_active(True)

    menu.append(item_rotnorm)
    menu.append(item_rotleft)
    menu.show_all()

    return menu

def rotleft(menuitem):
    subprocess.call(['xrandr', '--output', 'eDP1', '--rotate', 'left'])
    # menuitem.get_ancestor(Gtk.Menu).child_get("lapitem")[0].set_active(False)

def rotnorm(menuitem):
    subprocess.call(['xrandr', '--output', 'eDP1', '--rotate', 'normal'])
    # menuitem.get_ancestor(Gtk.Menu).child_get("readitem")[0].set_active(False)  

if __name__ == "__main__":
    indicator = appind.Indicator.new(
        "screen-rotator", os.path.abspath('science-book.svg'),
        appind.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appind.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()