kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5),
]

# Them san pham moi
kho_hang.append(("Tai nghe", 300000, 15))

# Xoa mot san pham
kho_hang.remove(("Chuot", 150000, 20))


print("--- DANH SÁCH SẢN PHẨM TRONG KHO ---")
for ten_sp, gia, so_luong in kho_hang:
    thanh_tien = gia * so_luong
    print(f"Sản phẩm: {ten_sp:<10} | Giá: {gia:>8} VNĐ | Số lượng: {so_luong:>2} | Thành tiền: {thanh_tien:>10} VNĐ")


tong_gia_tri_kho = 0
for ten_sp, gia, so_luong in kho_hang:
    tong_gia_tri_kho += gia * so_luong

print("-" * 36)
print(f"TỔNG GIÁ TRỊ KHO HÀNG: {tong_gia_tri_kho:,} VNĐ")