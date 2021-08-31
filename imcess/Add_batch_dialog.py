from PyQt5 import QtWidgets


class Add_batch_dialog(QtWidgets.QDialog):
    def __init__(self,dataStack,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add batch")
        self.layout = QtWidgets.QVBoxLayout()
        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.dataStack=dataStack
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.check_Validity)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Batch name:")
        self.text=QtWidgets.QLineEdit(parent)
        self.errorLabel= QtWidgets.QLabel("")
        self.layout.addWidget(message)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.errorLabel)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.exec_()
        print("test")

    def check_Validity(self):
        if not self.dataStack.batch_name_exists(self.text.text()) :
            self.name=self.text.text()
            self.accept()
        else:
            self.text.setText("")
            self.errorLabel.setText("Invalid name.")

        