# Enthought library imports.
from pyface.tasks.api import TraitsDockPane
from traits.api import Unicode
from traitsui.api import HTMLEditor, Item, View


class HelpPane(TraitsDockPane):
    """ A generic dock pane displaying a fixed HTML string.
    """

    #### 'ITaskPane' interface ################################################

    id = 'example.bare_bones.help_pane'
    name = 'Generic Information'

    #### 'ModelConfigPane' interface ##########################################

    html = Unicode

    view = View(Item('html',
                     editor=HTMLEditor(),
                     show_label=False),
                width=300,
                resizable=True)

    ###########################################################################
    # Protected interface.
    ###########################################################################

    def _html_default(self):
        return "This is a generic text."
