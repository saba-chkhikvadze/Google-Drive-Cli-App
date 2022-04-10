from app_brain import DriveAppBrain
from app_controller import DriveAppController
from cli import Cli


if __name__ == '__main__':
    brain = DriveAppBrain()
    view = Cli()
    controller = DriveAppController(view, brain)
    view.register_input_listener(controller)
    brain.register_display_changed_listener(view)
    controller.start()