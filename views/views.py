from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

from controllers import log

class main_frame(QMainWindow):
    def __init__(self):
        super().__init__()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        MainWindow.setToolTipDuration(-3)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tabs.setGeometry(QtCore.QRect(0, 0, 1031, 751))
        self.main_tabs.setObjectName("main_tabs")
        self.vocabulary = QtWidgets.QWidget()
        self.vocabulary.setObjectName("vocabulary")
        self.description = QtWidgets.QLabel(self.vocabulary)
        self.description.setGeometry(QtCore.QRect(420, 440, 431, 121))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std Light")
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.translation_label = QtWidgets.QLabel(self.vocabulary)
        self.translation_label.setGeometry(QtCore.QRect(540, 250, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std Light")
        font.setPointSize(24)
        font.setItalic(True)
        self.translation_label.setFont(font)
        self.translation_label.setObjectName("translation_label")
        self.example_sentence = QtWidgets.QLabel(self.vocabulary)
        self.example_sentence.setGeometry(QtCore.QRect(420, 310, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        self.example_sentence.setFont(font)
        self.example_sentence.setWordWrap(True)
        self.example_sentence.setObjectName("example_sentence")
        self.rel_header = QtWidgets.QLabel(self.vocabulary)
        self.rel_header.setGeometry(QtCore.QRect(450, 580, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rel_header.setFont(font)
        self.rel_header.setObjectName("rel_header")
        self.example_sentence_2 = QtWidgets.QLabel(self.vocabulary)
        self.example_sentence_2.setGeometry(QtCore.QRect(420, 350, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setItalic(True)
        self.example_sentence_2.setFont(font)
        self.example_sentence_2.setWordWrap(True)
        self.example_sentence_2.setObjectName("example_sentence_2")
        self.pos_label = QtWidgets.QLabel(self.vocabulary)
        self.pos_label.setGeometry(QtCore.QRect(420, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pos_label.setFont(font)
        self.pos_label.setObjectName("pos_label")
        self.description_header = QtWidgets.QLabel(self.vocabulary)
        self.description_header.setGeometry(QtCore.QRect(420, 400, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(14)
        self.description_header.setFont(font)
        self.description_header.setObjectName("description_header")
        self.word_label = QtWidgets.QLabel(self.vocabulary)
        self.word_label.setGeometry(QtCore.QRect(420, 190, 441, 51))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Std")
        font.setPointSize(36)
        self.word_label.setFont(font)
        self.word_label.setObjectName("word_label")
        self.word_image = QtWidgets.QGraphicsView(self.vocabulary)
        self.word_image.setGeometry(QtCore.QRect(330, 0, 691, 161))
        self.word_image.setObjectName("word_image")
        self.vocab_tv = QtWidgets.QTreeView(self.vocabulary)
        self.vocab_tv.setGeometry(QtCore.QRect(0, 0, 331, 681))
        self.vocab_tv.setObjectName("vocab_tv")
        self.vocab_tv.setStyleSheet("border: none;\n"
                                    "background-color: #eee;")
        self.vocab_tv.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(self.vocabulary)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(450, 610, 391, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rel5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel5.setFont(font)
        self.rel5.setText("")
        self.rel5.setObjectName("rel5")
        self.gridLayout.addWidget(self.rel5, 1, 0, 1, 1)
        self.rel7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel7.setFont(font)
        self.rel7.setText("")
        self.rel7.setObjectName("rel7")
        self.gridLayout.addWidget(self.rel7, 1, 2, 1, 1)
        self.rel1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel1.setFont(font)
        self.rel1.setText("")
        self.rel1.setObjectName("rel1")
        self.gridLayout.addWidget(self.rel1, 0, 0, 1, 1)
        self.rel6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel6.setFont(font)
        self.rel6.setText("")
        self.rel6.setObjectName("rel6")
        self.gridLayout.addWidget(self.rel6, 1, 1, 1, 1)
        self.rel2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel2.setFont(font)
        self.rel2.setText("")
        self.rel2.setObjectName("rel2")
        self.gridLayout.addWidget(self.rel2, 0, 1, 1, 1)
        self.rel3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel3.setFont(font)
        self.rel3.setText("")
        self.rel3.setObjectName("rel3")
        self.gridLayout.addWidget(self.rel3, 0, 2, 1, 1)
        self.rel4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel4.setFont(font)
        self.rel4.setText("")
        self.rel4.setObjectName("rel4")
        self.gridLayout.addWidget(self.rel4, 0, 3, 1, 1)
        self.rel8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica LT Std")
        font.setPointSize(10)
        self.rel8.setFont(font)
        self.rel8.setText("")
        self.rel8.setObjectName("rel8")
        self.gridLayout.addWidget(self.rel8, 1, 3, 1, 1)
        self.word_toolbox = QtWidgets.QStackedWidget(self.vocabulary)
        self.word_toolbox.setGeometry(QtCore.QRect(0, 690, 331, 31))
        self.word_toolbox.setObjectName("word_toolbox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.add_word = QtWidgets.QPushButton(self.page_3)
        self.add_word.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.add_word.setObjectName("add_word")
        self.del_word = QtWidgets.QPushButton(self.page_3)
        self.del_word.setGeometry(QtCore.QRect(70, 0, 71, 31))
        self.del_word.setObjectName("del_word")
        self.edit_word = QtWidgets.QPushButton(self.page_3)
        self.edit_word.setGeometry(QtCore.QRect(140, 0, 71, 31))
        self.edit_word.setObjectName("edit_word")
        self.word_toolbox.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.word_toolbox.addWidget(self.page_4)
        self.vocab_toolbox = QtWidgets.QToolBox(self.vocabulary)
        self.vocab_toolbox.setGeometry(QtCore.QRect(898, 190, 101, 281))
        self.vocab_toolbox.setStyleSheet("selection-color: rgb(0, 234, 86);")
        self.vocab_toolbox.setObjectName("vocab_toolbox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 101, 227))
        self.page.setObjectName("page")
        self.new_vocab = QtWidgets.QPushButton(self.page)
        self.new_vocab.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.new_vocab.setObjectName("new_vocab")
        self.open_vocab = QtWidgets.QPushButton(self.page)
        self.open_vocab.setGeometry(QtCore.QRect(0, 40, 101, 31))
        self.open_vocab.setObjectName("open_vocab")
        self.vocab_toolbox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 101, 227))
        self.page_2.setObjectName("page_2")
        self.import_btn = QtWidgets.QPushButton(self.page_2)
        self.import_btn.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.import_btn.setObjectName("import_btn")
        self.export_btn = QtWidgets.QPushButton(self.page_2)
        self.export_btn.setGeometry(QtCore.QRect(0, 40, 101, 31))
        self.export_btn.setObjectName("export_btn")
        self.populate_btn = QtWidgets.QPushButton(self.page_2)
        self.populate_btn.setGeometry(QtCore.QRect(0, 80, 101, 31))
        self.populate_btn.setObjectName("populate_btn")
        self.stats_btn = QtWidgets.QPushButton(self.page_2)
        self.stats_btn.setGeometry(QtCore.QRect(0, 120, 101, 31))
        self.stats_btn.setObjectName("stats_btn")
        self.vocab_toolbox.addItem(self.page_2, "")
        self.main_tabs.addTab(self.vocabulary, "")
        self.construction = QtWidgets.QWidget()
        self.construction.setObjectName("construction")
        self.horizontalSlider = QtWidgets.QSlider(self.construction)
        self.horizontalSlider.setGeometry(QtCore.QRect(600, 20, 231, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.construction)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(600, 80, 231, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.construction)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(600, 140, 231, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.constr_toolbox = QtWidgets.QToolBox(self.construction)
        self.constr_toolbox.setGeometry(QtCore.QRect(890, 20, 101, 281))
        self.constr_toolbox.setObjectName("constr_toolbox")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 101, 227))
        self.page_5.setObjectName("page_5")
        self.new_vocab_2 = QtWidgets.QPushButton(self.page_5)
        self.new_vocab_2.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.new_vocab_2.setObjectName("new_vocab_2")
        self.constr_toolbox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 101, 227))
        self.page_6.setObjectName("page_6")
        self.feed_text = QtWidgets.QPushButton(self.page_6)
        self.feed_text.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.feed_text.setObjectName("feed_text")
        self.constr_toolbox.addItem(self.page_6, "")
        self.dial = QtWidgets.QDial(self.construction)
        self.dial.setGeometry(QtCore.QRect(700, 200, 50, 64))
        self.dial.setObjectName("dial")
        self.main_tabs.addTab(self.construction, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Vocabulary = QtWidgets.QAction(MainWindow)
        self.actionOpen_Vocabulary.setObjectName("actionOpen_Vocabulary")
        self.actionNew_Vocabulary = QtWidgets.QAction(MainWindow)
        self.actionNew_Vocabulary.setObjectName("actionNew_Vocabulary")
        self.actionClose_Vocabulary = QtWidgets.QAction(MainWindow)
        self.actionClose_Vocabulary.setObjectName("actionClose_Vocabulary")
        self.actionQuit_Program = QtWidgets.QAction(MainWindow)
        self.actionQuit_Program.setObjectName("actionQuit_Program")
        self.actionImport_xls_csv = QtWidgets.QAction(MainWindow)
        self.actionImport_xls_csv.setObjectName("actionImport_xls_csv")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionPopulate_Vocabulary = QtWidgets.QAction(MainWindow)
        self.actionPopulate_Vocabulary.setObjectName("actionPopulate_Vocabulary")
        self.actionShow_Stats = QtWidgets.QAction(MainWindow)
        self.actionShow_Stats.setObjectName("actionShow_Stats")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionFeed_Text = QtWidgets.QAction(MainWindow)
        self.actionFeed_Text.setObjectName("actionFeed_Text")

        self.retranslateUi(MainWindow)
        self.main_tabs.setCurrentIndex(0)
        self.word_toolbox.setCurrentIndex(0)
        self.vocab_toolbox.setCurrentIndex(1)
        self.constr_toolbox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Language Construction Tool"))
        self.main_tabs.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.description.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."))
        self.translation_label.setText(_translate("MainWindow", "Translation"))
        self.example_sentence.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."))
        self.rel_header.setText(_translate("MainWindow", "Related Words"))
        self.example_sentence_2.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."))
        self.pos_label.setText(_translate("MainWindow", "Verb"))
        self.description_header.setText(_translate("MainWindow", "Description"))
        self.word_label.setText(_translate("MainWindow", "Word Item"))
        self.add_word.setText(_translate("MainWindow", "Add Word"))
        self.del_word.setText(_translate("MainWindow", "Del Word"))
        self.edit_word.setText(_translate("MainWindow", "Edit Word"))
        self.new_vocab.setText(_translate("MainWindow", "New Vocab"))
        self.open_vocab.setText(_translate("MainWindow", "Open Vocab"))
        self.vocab_toolbox.setItemText(self.vocab_toolbox.indexOf(self.page), _translate("MainWindow", "File"))
        self.import_btn.setText(_translate("MainWindow", "Import xls/csv"))
        self.export_btn.setText(_translate("MainWindow", "Export..."))
        self.populate_btn.setText(_translate("MainWindow", "Populate..."))
        self.stats_btn.setText(_translate("MainWindow", "Show Stats"))
        self.vocab_toolbox.setItemText(self.vocab_toolbox.indexOf(self.page_2), _translate("MainWindow", "Vocabulary"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.vocabulary), _translate("MainWindow", "Vocabulary"))
        self.new_vocab_2.setText(_translate("MainWindow", "New Vocab"))
        self.constr_toolbox.setItemText(self.constr_toolbox.indexOf(self.page_5), _translate("MainWindow", "Construction"))
        self.feed_text.setText(_translate("MainWindow", "Feed Text"))
        self.constr_toolbox.setItemText(self.constr_toolbox.indexOf(self.page_6), _translate("MainWindow", "Text Tools"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.construction), _translate("MainWindow", "Construction"))
        self.actionOpen_Vocabulary.setText(_translate("MainWindow", "Open Vocabulary"))
        self.actionNew_Vocabulary.setText(_translate("MainWindow", "New Vocabulary"))
        self.actionClose_Vocabulary.setText(_translate("MainWindow", "Close Vocabulary"))
        self.actionQuit_Program.setText(_translate("MainWindow", "Quit Program"))
        self.actionImport_xls_csv.setText(_translate("MainWindow", "Import xls/csv"))
        self.actionExport.setText(_translate("MainWindow", "Export..."))
        self.actionPopulate_Vocabulary.setText(_translate("MainWindow", "Populate Vocabulary..."))
        self.actionShow_Stats.setText(_translate("MainWindow", "Show Stats"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionFeed_Text.setText(_translate("MainWindow", "Feed Text..."))
