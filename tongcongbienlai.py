# Danh sách các mặt hàng trong biên lai
cac_muc_hang = [
    {'ten': 'Sách A', 'so_luong': 2, 'don_gia': 150000, 'tong_tien': 300000},
    {'ten': 'Bút B', 'so_luong': 10, 'don_gia': 5000, 'tong_tien': 50000},
    {'ten': 'Tập C', 'so_luong': 5, 'don_gia': 12000, 'tong_tien': 60000}
]

# Khởi tạo biến tổng cộng
tong_cong_thanh_toan = 0

# Dùng vòng lặp để cộng dồn tổng tiền từng mặt hàng
for item in cac_muc_hang:
    tong_cong_thanh_toan += item['tong_tien']

# In ra tổng cộng của biên lai với 2 chữ số thập phân
print(f"Tổng cộng biên lai: {tong_cong_thanh_toan:.2f} VND")