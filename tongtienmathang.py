# Danh sách các mặt hàng
mat_hang = [
    {"ten": "Bút bi", "so_luong": 10, "don_gia": 5000},
    {"ten": "Vở học sinh", "so_luong": 5, "don_gia": 12000},
    {"ten": "Thước kẻ", "so_luong": 2, "don_gia": 8000},
]

# In tiêu đề
print("{:<20} {:>10} {:>15} {:>20}".format("Tên mặt hàng", "Số lượng", "Đơn giá (VNĐ)", "Thành tiền (VNĐ)"))

# Tính toán và in từng dòng
tong_cong = 0
for hang in mat_hang:
    thanh_tien = hang["so_luong"] * hang["don_gia"]
    tong_cong += thanh_tien
    print("{:<20} {:>10} {:>15,} {:>20,}".format(hang["ten"], hang["so_luong"], hang["don_gia"], thanh_tien))

# In tổng cộng
print("-" * 70)
print("{:<20} {:>10} {:>15} {:>20,}".format("Tổng cộng", "", "", tong_cong))