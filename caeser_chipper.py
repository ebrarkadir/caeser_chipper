import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

class CaesarCipherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caesar Cipher')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        input_frame = QFrame(self)
        input_frame.setStyleSheet("background-color: #f0f0f0; border-radius: 5px;")
        input_layout = QHBoxLayout()
        input_frame.setLayout(input_layout)
        layout.addWidget(input_frame)

        self.input_label = QLabel("Yazı:", self)
        input_layout.addWidget(self.input_label)

        self.input_text = QLineEdit(self)
        input_layout.addWidget(self.input_text)

        self.shift_label = QLabel("Atlama:", self)
        input_layout.addWidget(self.shift_label)

        self.shift_text = QLineEdit(self)
        input_layout.addWidget(self.shift_text)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.encrypt_button = QPushButton("Encrypt", self)
        self.encrypt_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 15px;")
        self.encrypt_button.clicked.connect(self.encrypt_text)
        button_layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt", self)
        self.decrypt_button.setStyleSheet("background-color: #f44336; color: white; border-radius: 15px;")
        self.decrypt_button.clicked.connect(self.decrypt_text)
        button_layout.addWidget(self.decrypt_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

    def encrypt_text(self):
        text = self.input_text.text()
        shift_text = self.shift_text.text()
        if not text:
            QMessageBox.warning(self, "Input Error", "Lütfen Yazı Giriniz.")
            return
        if not shift_text:
            QMessageBox.warning(self, "Input Error", "Lütfen Atlama Giriniz.")
            return
        shift = int(shift_text)
        encrypted_text = caesar_cipher(text, shift)
        QMessageBox.information(self, "Encryption Sonucu", f"Encrypted Yazı: {encrypted_text}")
        
    def decrypt_text(self):
        text = self.input_text.text()
        shift_text = self.shift_text.text()
        if not text:
            QMessageBox.warning(self, "Input Error", "Lütfen Yazı Giriniz.")
            return
        if not shift_text:
            QMessageBox.warning(self, "Input Error", "Lütfen Atlama Giriniz.")
            return
        shift = int(shift_text)
        decrypted_text = caesar_cipher(text, -shift)
        QMessageBox.information(self, "Decryption Sonucu", f"Decrypted Yazı: {decrypted_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaesarCipherUI()
    window.setStyleSheet("background-color: #ffffff;")
    window.show()
    sys.exit(app.exec_())
