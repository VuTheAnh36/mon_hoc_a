import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, 
    QGridLayout, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("Máy tính bỏ túi - PySide6")
        self.resize(300, 400)

        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet("font-size: 24px; padding: 10px;")

        luoi_nut = QGridLayout()

        cac_nut = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]

        for text, hang, cot in cac_nut:
            nut = QPushButton(text)
            nut.setStyleSheet("font-size: 18px; padding: 15px;")
            if text == '=':
                nut.clicked.connect(self.tinh_ket_qua)
            elif text == 'C':
                nut.clicked.connect(self.xoa_man_hinh)
            else:
                nut.clicked.connect(lambda checked=False, t=text: self.them_ky_tu(t))
            
            if text == '=':
                luoi_nut.addWidget(nut, hang, cot, 1, 2)
            else:
                luoi_nut.addWidget(nut, hang, cot)

        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)
        layout_chinh.addLayout(luoi_nut)
        self.setLayout(layout_chinh)

    def them_ky_tu(self, ky_tu):
        hien_tai = self.man_hinh.text()
        self.man_hinh.setText(hien_tai + ky_tu)

    def xoa_man_hinh(self):
        self.man_hinh.clear()

    def tinh_ket_qua(self):
        bieu_thuc = self.man_hinh.text()
        try:
            ket_qua = str(eval(bieu_thuc))
            self.man_hinh.setText(ket_qua)
        except Exception:
            QMessageBox.critical(self, "Lỗi", "Biểu thức không hợp lệ!")
            self.man_hinh.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec())