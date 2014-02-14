# Set up the default toolkit.
from traits.etsconfig.api import ETSConfig
ETSConfig.toolkit = 'qt4'

# Standard library imports.
import logging
import argparse

# Plugin imports.
from envisage.core_plugin import CorePlugin
from envisage.ui.tasks.tasks_plugin import TasksPlugin
from bare_bones_plugin import BareBonesPlugin

# Local imports.
from bare_bones_application import BareBonesApplication


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description="A generic Tasks application",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose logging."
    )
    parser.add_argument(
        "-d", "--dummy",
        help="A dummy command-line argument."
    )
    return parser.parse_args()


def main():
    """ Run the application.
    """
    # Process command-line arguments.
    args = parse_command_line_args()

    # Set up logging.
    if args.verbose:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.WARNING
    logging.basicConfig(level=logging_level)

    # Build the application and run it.
    plugins = [CorePlugin(), TasksPlugin(), BareBonesPlugin()]
    app = BareBonesApplication(plugins=plugins)
    app.run()

    logging.shutdown()


if __name__ == '__main__':
    main()
