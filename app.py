from PyQt5.QtWidgets import QApplication
from controllers.ctrls import lct_controller
from views.main_frame import main_frame
from controllers import log
from controllers import utils

import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        conf = utils.Config()
        self.main_win = main_frame()
        self.main_win.setupUi(self.main_win)
        self.main_controller = lct_controller(self.main_win, start_up=True)
        log.debug("GUI: Starting Main Frame")
        self.main_win.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

