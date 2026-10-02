
danh_sach_sach = [
    {
        "ma_sach": "S001",
        "tieu_de": "Lap Trinh Python Can Ban",
        "tac_gia": "Nguyen Van A",
        "trang_thai": "Co san",
        "nguoi_muon": "",
    },
    {
        "ma_sach": "S002",
        "tieu_de": "Cau Truc Du Lieu Va Giai Thuat",
        "tac_gia": "Tran Van B",
        "trang_thai": "Co san",
        "nguoi_muon": "",
    },
    {
        "ma_sach": "S003",
        "tieu_de": "Co So Du Lieu MySQL",
        "tac_gia": "Le Thi C",
        "trang_thai": "Co san",
        "nguoi_muon": "",
    },
    {
        "ma_sach": "S004",
        "tieu_de": "Lap Trinh Huong Doi Tuong Java",
        "tac_gia": "Pham Van D",
        "trang_thai": "Co san",
        "nguoi_muon": "",
    },
]

lich_su_muon_tra = []



def hien_thi_danh_sach_sach():
  print("\n" + "=" * 85)
  header = (
      f"{'Ma sach':<10}"
      f"{'Tieu de sach':<32}"
      f"{'Tac gia':<20}"
      f"{'Trang thai':<12}"
      f"{'Nguoi muon':<15}"
  )
  print(header)
  print("-" * 85)
  for sach in danh_sach_sach:
    dong = (
        f"{sach['ma_sach']:<10}"
        f"{sach['tieu_de']:<32}"
        f"{sach['tac_gia']:<20}"
        f"{sach['trang_thai']:<12}"
        f"{sach['nguoi_muon']:<15}"
    )
    print(dong)
  print("=" * 85)


# Hàm hỗ trợ tìm kiếm sách theo mã
def tim_sach_theo_ma(ma_sach):
  for sach in danh_sach_sach:
    if sach["ma_sach"] == ma_sach:
      return sach
  return None


def xem_sach_co_san():
  sach_co_san = [
      sach for sach in danh_sach_sach if sach["trang_thai"] == "Co san"
  ]
  if len(sach_co_san) == 0:
    print("-> Hien khong con sach nao co san de muon.")
    return
  print("\nCAC SACH DANG CO SAN:")
  for sach in sach_co_san:
    print(
        f" - [{sach['ma_sach']}] {sach['tieu_de']} (Tac gia: {sach['tac_gia']})"
    )


def them_sach(ma_sach, tieu_de, tac_gia):
  if tim_sach_theo_ma(ma_sach) is not None:
    print(f"-> Ma sach {ma_sach} da ton tai, khong the them.")
    return
  danh_sach_sach.append({
      "ma_sach": ma_sach,
      "tieu_de": tieu_de,
      "tac_gia": tac_gia,
      "trang_thai": "Co san",
      "nguoi_muon": "",
  })
  print(f"-> Da them sach {ma_sach} thanh cong.")


def muon_sach(ma_sach, ten_nguoi_muon):
  sach = tim_sach_theo_ma(ma_sach)
  if sach is None:
    print(f"-> Khong tim thay sach {ma_sach}.")
    return
  if sach["trang_thai"] == "Dang muon":
    print(f"-> Sach {ma_sach} dang duoc nguoi khac muon, khong the muon.")
    return

  sach["trang_thai"] = "Dang muon"
  sach["nguoi_muon"] = ten_nguoi_muon
  print(f"-> Muon sach {ma_sach} cho ban {ten_nguoi_muon} thanh cong.")


def tra_sach(ma_sach, so_ngay_muon):
  sach = tim_sach_theo_ma(ma_sach)
  if sach is None:
    print(f"-> Khong tim thay sach {ma_sach}.")
    return
  if sach["trang_thai"] == "Co san":
    print(f"-> Sach {ma_sach} dang co san, khong co ai de tra.")
    return

  tien_phat = 0
  if so_ngay_muon > 7:
    tien_phat = (so_ngay_muon - 7) * 5000

  lich_su_muon_tra.append({
      "ma_sach": ma_sach,
      "tieu_de": sach["tieu_de"],
      "nguoi_muon": sach["nguoi_muon"],
      "so_ngay_muon": so_ngay_muon,
      "tien_phat": tien_phat,
  })

  print(
      f"-> Ban {sach['nguoi_muon']} da tra sach {ma_sach} sau {so_ngay_muon}"
      " ngay."
  )
  if tien_phat > 0:
    print(f"-> Sach bi qua han! Tien phat: {tien_phat:,} VND")
  else:
    print("-> Tra sach dung han, khong co tien phat.")

  sach["trang_thai"] = "Co san"
  sach["nguoi_muon"] = ""


def thong_ke_lich_su():
  if len(lich_su_muon_tra) == 0:
    print("-> Chua co giao dich tra sach nao.")
    return
  tong_tien_phat = 0
  print("\nLICH SU MUON TRA SACH:")
  for gd in lich_su_muon_tra:
    print(
        f" - [{gd['ma_sach']}] {gd['tieu_de']} | Nguoi muon: {gd['nguoi_muon']}"
        f" | {gd['so_ngay_muon']} ngay | Tien phat: {gd['tien_phat']:,} VND"
    )
    tong_tien_phat += gd["tien_phat"]
  print(f"\n>>> TONG TIEN PHAT THU DUOC: {tong_tien_phat:,} VND")


def nhap_so_nguyen(loi_nhac):
  while True:
    try:
      return int(input(loi_nhac))
    except ValueError:
      print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def hien_thi_menu():
  print("\n===== QUAN LY THU VIEN SACH =====")
  print("1. Hien thi danh sach tat ca sach")
  print("2. Xem cac sach dang co san de muon")
  print("3. Them sach moi vao thu vien")
  print("4. Muon sach")
  print("5. Tra sach")
  print("6. Thong ke lich su & tien phat")
  print("0. Thoat chuong trinh")


def chay_chuong_trinh():
  while True:
    hien_thi_menu()
    lua_chon = input("Nhap lua chon cua ban: ").strip()
    if lua_chon == "1":
      hien_thi_danh_sach_sach()
    elif lua_chon == "2":
      xem_sach_co_san()
    elif lua_chon == "3":
      ma_sach = input("Nhap ma sach moi: ").strip().upper()
      tieu_de = input("Nhap tieu de sach: ").strip().title()
      tac_gia = input("Nhap ten tac gia: ").strip().title()
      them_sach(ma_sach, tieu_de, tac_gia)
    elif lua_chon == "4":
      ma_sach = input("Nhap ma sach can muon: ").strip().upper()
      ten_nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
      muon_sach(ma_sach, ten_nguoi_muon)
    elif lua_chon == "5":
      ma_sach = input("Nhap ma sach can tra: ").strip().upper()
      so_ngay_muon = nhap_so_nguyen("Nhap so ngay da muon: ")
      tra_sach(ma_sach, so_ngay_muon)
    elif lua_chon == "6":
      thong_ke_lich_su()
    elif lua_chon == "0":
      print("Cam on da su dung chuong trinh. Tam biet!")
      break
    else:
      print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
  chay_chuong_trinh()