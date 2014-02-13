# Standard library imports.
import logging

# Plugin imports.
from envisage.core_plugin import CorePlugin
from envisage.ui.tasks.tasks_plugin import TasksPlugin
from bare_bones_plugin import BareBonesPlugin

# Local imports.
from bare_bones_application import BareBonesApplication


def main(argv):
    """ Run the application.
    """
    logging.basicConfig(level=logging.DEBUG)

    plugins = [CorePlugin(), TasksPlugin(), BareBonesPlugin()]
    app = BareBonesApplication(plugins=plugins)
    app.run()

    logging.shutdown()


if __name__ == '__main__':
    import sys
    main(sys.argv)
