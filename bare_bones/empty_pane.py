# Enthought library imports.
from pyface.tasks.api import TraitsTaskPane
from traitsui.api import HGroup, Label, View


class EmptyPane(TraitsTaskPane):

    #### 'ITaskPane' interface ################################################

    id = 'example.bare_bones.empty_pane'
    name = 'Empty Pane'

    view = View(HGroup(Label('This is the central pane')))
