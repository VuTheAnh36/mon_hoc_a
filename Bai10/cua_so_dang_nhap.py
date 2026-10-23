import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        
        thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
        duong_dan_ui = os.path.join(thu_muc_hien_tai, "form_dang_nhap.ui")
        
        file_ui = QFile(duong_dan_ui)
        if not file_ui.open(QFile.ReadOnly):
            sys.exit(1)
            
        loader = QUiLoader()
        self.ui = loader.load(file_ui, self)
        file_ui.close()
        
        self.resize(self.ui.size())
        self.setWindowTitle("Đăng nhập")
        
        self.ui.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.ui.o_nhap_tai_khoan.text()
        mat_khau = self.ui.o_nhap_mat_khau.text()
        
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return
            
        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec())