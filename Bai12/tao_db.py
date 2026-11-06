import sqlite3

ket_noi = sqlite3.connect("tu_dien.db")
con_tro = ket_noi.cursor()

con_tro.execute("""
CREATE TABLE IF NOT EXISTS tu_dien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tu TEXT NOT NULL,
    loai_tu TEXT NOT NULL,
    nghia TEXT NOT NULL,
    vi_du TEXT
)
""")

tu_vung_mau = [
    ("Python", "Danh tu (Noun)", "Một ngôn ngữ lập trình bậc cao, thông dịch, hướng đối tượng.", "Python is widely used in AI and web development."),
    ("Database", "Danh tu (Noun)", "Cơ sở dữ liệu, tập hợp thông tin có tổ chức.", "The application stores records in a SQLite database."),
    ("Develop", "Dong tu (Verb)", "Phát triển, xây dựng phần mềm hoặc ứng dụng.", "Our team is developing a desktop application using Tkinter."),
    ("Efficient", "Tinh tu (Adjective)", "Hiệu quả, tối ưu hóa thời gian và tài nguyên.", "Modular programming makes code maintenance more efficient."),
    ("Algorithm", "Danh tu (Noun)", "Thuật toán, tập hợp các bước giải quyết vấn đề.", "The search algorithm quickly retrieves dictionary entries.")
]

con_tro.execute("DELETE FROM tu_dien")
con_tro.executemany(
    "INSERT INTO tu_dien (tu, loai_tu, nghia, vi_du) VALUES (?, ?, ?, ?)",
    tu_vung_mau
)

ket_noi.commit()
ket_noi.close()
print("Đã tạo thành công file tu_dien.db với dữ liệu mẫu!")