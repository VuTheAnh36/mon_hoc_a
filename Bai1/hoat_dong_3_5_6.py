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

a = 17
b = 5

print("a + b  =", a + b)   
print("a - b  =", a - b)   
print("a * b  =", a * b)   
print("a / b  =", a / b)   
print("a // b =", a // b)  
print("a % b  =", a % b)   
print("a ** b =", a ** b)  
diem = 6.5
tuoi = 20


la_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm có đạt loại Khá không?:", la_kha)


ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Tuoi chưa đủ 18 hoặc trên 60 không?:", ngoai_do_tuoi_lao_dong)


print("Phủ định điều kiện loại Khá:", not la_kha)
print("Phủ định điều kiện ngoài độ tuổi:", not ngoai_do_tuoi_lao_dong)

x = 10
print("Ban đầu: x =", x)

x += 5   
print("x += 5  -> x =", x)   

x -= 3   
print("x -= 3  -> x =", x)   

x *= 2   
print("x *= 2  -> x =", x)   
x /= 4   
print("x /= 4  -> x =", x)   

x //= 2  
print("x //= 2 -> x =", x)  

x **= 3  
print("x **= 3 -> x =", x)   


danh_sach = [1, 2, 3, "python"]
kiem_tra = 3 in danh_sach
print("3 có nằm trong danh_sach không?:", kiem_tra)  


list_a = [1, 2, 3]
list_b = list_a  

print("list_a is list_b?:", list_a is list_b)  

bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))


ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0


dtb = (diem_toan + diem_ly + diem_hoa) / 3


la_gioi = dtb >= 8.0
la_kha = (dtb >= 6.5) and (dtb < 8.0)
la_trung_binh = (dtb >= 5.0) and (dtb < 6.5)
la_yeu = dtb < 5.0


print("Họ và tên:", ho_ten)
print("Điểm trung bình:", round(dtb, 2))
print("----------------------------")
print("Đạt loại Giỏi?:", la_gioi)
print("Đạt loại Khá?:", la_kha)
print("Đạt loại Trung bình?:", la_trung_binh)
print("Đạt loại Yếu?:", la_yeu)
print("----------------------------")
print("Kiểu dữ liệu của biến la_gioi:", type(la_gioi))