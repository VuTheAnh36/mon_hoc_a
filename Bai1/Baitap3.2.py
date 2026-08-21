ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2

MUC_LUONG_TOI_THIEU = 5000000

diem_trung_binh = (diem_toan + diem_van) / so_luong_mon_hoc

print("=== THÔNG TIN SINH VIÊN ===")
print(f"Họ và tên: {ten}")
print(f"Điểm Toán: {diem_toan}")
print(f"Điểm Văn: {diem_van}")
print(f"Số lượng môn học: {so_luong_mon_hoc}")
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Mức lương tối thiểu: {MUC_LUONG_TOI_THIEU:,} VNĐ")