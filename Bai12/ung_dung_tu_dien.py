import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_tu_dien as db

DANH_SACH_LOAI_TU = ["Danh tu (Noun)", "Dong tu (Verb)", "Tinh tu (Adjective)", "Trang tu (Adverb)", "Khac"]

class UngDungTuDien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tu dien tra cuu ca nhan")
        self.geometry("640x520")
        self.resizable(False, False)
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(self, text=" Thong tin tu vung ", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tu vung:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_tu = tk.Entry(khung_nhap, width=24)
        self.o_nhap_tu.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loai tu:").grid(row=0, column=2, sticky="w", pady=5)
        self.chon_loai_tu = ttk.Combobox(khung_nhap, values=DANH_SACH_LOAI_TU, width=22, state="readonly")
        self.chon_loai_tu.current(0)
        self.chon_loai_tu.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(khung_nhap, text="Nghia:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_nghia = tk.Entry(khung_nhap, width=24)
        self.o_nhap_nghia.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Vi du:").grid(row=1, column=2, sticky="w", pady=5)
        self.o_nhap_vi_du = tk.Entry(khung_nhap, width=24)
        self.o_nhap_vi_du.grid(row=1, column=3, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them tu moi", bg="lightgreen", command=self.xu_ly_them_tu).grid(row=2, column=0, columnspan=4, pady=10)

        khung_tim_kiem = tk.Frame(self)
        khung_tim_kiem.pack(pady=5, padx=10, fill="x")
        tk.Label(khung_tim_kiem, text="Tra cuu:").pack(side="left", padx=5)
        self.o_nhap_tim_kiem = tk.Entry(khung_tim_kiem, width=35)
        self.o_nhap_tim_kiem.pack(side="left", padx=5)
        tk.Button(khung_tim_kiem, text="Tim kiem", command=self.xu_ly_tim_kiem).pack(side="left", padx=5)
        tk.Button(khung_tim_kiem, text="Tat ca", command=self.tai_lai_danh_sach).pack(side="left", padx=5)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)
        self.listbox_tu = tk.Listbox(khung_danh_sach, width=82, height=13)
        self.listbox_tu.pack(side="left", fill="both", expand=True)
        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_tu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_tu.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)
        tk.Button(khung_nut, text="Xoa tu", bg="lightcoral", command=self.xu_ly_xoa_tu).grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Thong ke loai tu", bg="lightblue", command=self.xu_ly_thong_ke).grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_tu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_tu()
        for item in self.danh_sach_hien_tai:
            id_tu, tu, loai_tu, nghia, vi_du = item
            self.listbox_tu.insert(tk.END, f"{tu} [{loai_tu}] : {nghia} | VD: {vi_du}")

    def xu_ly_them_tu(self):
        tu = self.o_nhap_tu.get().strip()
        loai_tu = self.chon_loai_tu.get()
        nghia = self.o_nhap_nghia.get().strip()
        vi_du = self.o_nhap_vi_du.get().strip()

        if tu == "" or nghia == "":
            messagebox.showerror("Loi", "Vui long nhap day du tu vung va nghia.")
            return
        
        db.them_tu(tu, loai_tu, nghia, vi_du)
        self.o_nhap_tu.delete(0, tk.END)
        self.o_nhap_nghia.delete(0, tk.END)
        self.o_nhap_vi_du.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them tu: {tu}")

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_nhap_tim_kiem.get().strip()
        if tu_khoa == "":
            self.tai_lai_danh_sach()
            return
        self.listbox_tu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.tim_kiem_tu(tu_khoa)
        for item in self.danh_sach_hien_tai:
            id_tu, tu, loai_tu, nghia, vi_du = item
            self.listbox_tu.insert(tk.END, f"{tu} [{loai_tu}] : {nghia} | VD: {vi_du}")

    def xu_ly_xoa_tu(self):
        lua_chon = self.listbox_tu.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot tu trong danh sach de xoa.")
            return
        id_tu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_tu(id_tu)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da xoa tu khoi tu dien.")

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_loai_tu()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu tu vung de thong ke.")
            return
        cac_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_loai, so_luong, color="teal")
        plt.title("Thong ke so luong tu vung theo loai tu")
        plt.xlabel("Loai tu")
        plt.ylabel("So luong")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungTuDien()
    ung_dung.mainloop()