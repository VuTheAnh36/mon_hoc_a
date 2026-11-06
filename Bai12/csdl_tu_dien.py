import sqlite3

TEN_FILE_CSDL = "tu_dien.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
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
    ket_noi.commit()
    ket_noi.close()

def them_tu(tu, loai_tu, nghia, vi_du):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO tu_dien (tu, loai_tu, nghia, vi_du) VALUES (?, ?, ?, ?)",
        (tu, loai_tu, nghia, vi_du)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_tu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, tu, loai_tu, nghia, vi_du FROM tu_dien ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def tim_kiem_tu(tu_khoa):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT id, tu, loai_tu, nghia, vi_du FROM tu_dien WHERE tu LIKE ? OR nghia LIKE ?",
        (f"%{tu_khoa}%", f"%{tu_khoa}%")
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_tu(id_tu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM tu_dien WHERE id = ?", (id_tu,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_loai_tu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT loai_tu, COUNT(*) FROM tu_dien GROUP BY loai_tu")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua