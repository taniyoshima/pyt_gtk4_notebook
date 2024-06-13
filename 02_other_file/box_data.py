import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_note1.ui')
class NotebookChild(Gtk.Box):

    __gtype_name__ = "notebook_child"

    def __init__(self):
        Gtk.Box.__init__(self)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        print('Button Clicked')
