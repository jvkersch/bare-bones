# Enthought library imports.
from pyface.tasks.action.api import SMenu, SMenuBar, TaskToggleGroup
from pyface.tasks.api import Task, TaskLayout, Tabbed, PaneItem

# Local imports.
from help_pane import HelpPane
from empty_pane import EmptyPane


class BareBonesTask(Task):
    """ A bare-bones task.
    """

    #### 'Task' interface #####################################################

    id = 'example.bare_bones.task'
    name = 'Bare-bones Task'

    menu_bar = SMenuBar(SMenu(id='File', name='&File'),
                        SMenu(id='Edit', name='&Edit'),
                        SMenu(TaskToggleGroup(),
                              id='View', name='&View'))

    ###########################################################################
    # 'Task' interface.
    ###########################################################################

    def create_central_pane(self):
        return EmptyPane()

    def create_dock_panes(self):
        return [HelpPane()]

    ###########################################################################
    # Protected interface.
    ###########################################################################

    #### Trait initializers ###################################################

    def _default_layout_default(self):
        return TaskLayout(
            left=Tabbed(PaneItem('example.bare_bones.help_pane'))
        )
