# Standard library imports.
import logging

# Plugin imports.
from envisage.core_plugin import CorePlugin
from envisage.ui.tasks.tasks_plugin import TasksPlugin
from bare_bones_plugin import BareBonesPlugin

# Local imports.
from bare_bones_application import BareBonesApplication


def main():
    """ Run the application.
    """
    # TODO: process command line arguments properly.

    logging.basicConfig(level=logging.DEBUG)

    plugins = [CorePlugin(), TasksPlugin(), BareBonesPlugin()]
    app = BareBonesApplication(plugins=plugins)
    app.run()

    logging.shutdown()


if __name__ == '__main__':
    main()
