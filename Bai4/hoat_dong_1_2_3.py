sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("Ho ten:", sinh_vien["ho_ten"])
print("Diem TB:", sinh_vien.get("diem_tb"))
print("Lop:", sinh_vien.get("lop", "Chua co"))

sinh_vien["lop"] = "CNTT01"
sinh_vien["diem_tb"] = 9.0
print("Sau khi them/sua:", sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")
print("Sau khi xoa:", sinh_vien, "- Diem da xoa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"})
print("Sau khi update:", sinh_vien)

diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

print("\nCac mon hoc:")
for mon in diem_mon_hoc.keys():
    print(mon)

print("\nCac diem so:")
for diem in diem_mon_hoc.values():
    print(diem)

print("\nChi tiet mon va diem:")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
dtb = tong_diem / len(diem_mon_hoc)
print("Diem trung binh cac mon:", round(dtb, 2))

diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print("\nDiem sau khi cong them 0.5:", diem_cong_diem)

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print("Ten mon viet hoa:", ten_mon_viet_hoa)

mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("Mon hoc chung 2 ky (Giao):", mon_hoc_ky1 & mon_hoc_ky2)
print("Tat ca mon hoc ca 2 ky (Hop):", mon_hoc_ky1 | mon_hoc_ky2)
print("Mon chi co o ky 1:", mon_hoc_ky1 - mon_hoc_ky2)