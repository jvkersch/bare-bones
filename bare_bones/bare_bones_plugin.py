# Standard library imports.
import os.path

# Enthought library imports.
from envisage.api import Plugin
from envisage.ui.tasks.api import TaskFactory
from traits.api import List


class BareBonesPlugin(Plugin):
    """ The bare bones plugin.
    """

    # Extension point IDs.
    PREFERENCES = 'envisage.preferences'

    PREFERENCES_PANES = 'envisage.ui.tasks.preferences_panes'

    TASKS = 'envisage.ui.tasks.tasks'

    #### 'IPlugin' interface ##################################################

    # The plugin's unique identifier.
    id = 'example.bare_bones'

    # The plugin's name (suitable for displaying to the user).
    name = 'BareBones'

    #### Contributions to extension points made by this plugin ################

    preferences = List(contributes_to=PREFERENCES)
    preferences_panes = List(contributes_to=PREFERENCES_PANES)
    tasks = List(contributes_to=TASKS)

    ###########################################################################
    # Protected interface.
    ###########################################################################

    def _preferences_default(self):
        filename = os.path.join(os.path.dirname(__file__), 'preferences.ini')
        return ['file://' + filename]

    def _preferences_panes_default(self):
        from bare_bones_preferences import BareBonesPreferencesPane
        return [BareBonesPreferencesPane]

    def _tasks_default(self):
        from bare_bones_task import BareBonesTask

        return [TaskFactory(id='example.bare_bones.task',
                            name='Bare-bones Task',
                            factory=BareBonesTask)]
