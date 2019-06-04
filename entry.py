#!/bin/python3
import gi
import sys
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, GLib, Gdk

# import printData function
from printData import printData

class EntryWindow(Gtk.Window):

    def __init__(self, master=None):
        Gtk.Window.__init__(self, title="Input")
        self.set_size_request(300, 50)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("")
        self.entry.set_editable(True)
        self.entry.connect("key-release-event", self.on_key_release) 
        self.entry.connect("activate", self.cb_activate)

        vbox.pack_start(self.entry, True, True, 0)
        hbox = Gtk.Box(spacing=6)
        Gtk.main_quit()




    def cb_activate(self, entry):
        inputData = entry.get_text()
        printData(inputData)
        entry.set_text("")
        
    def close(event):
        sys.exit() # if you want to exit the entire thing

    def on_key_release(self, widget, ev, data=None):
        if ev.keyval == Gdk.KEY_Escape: #If Escape pressed, reset text
            Gtk.main_quit()


if __name__ == "__main__":
    win = EntryWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
