# Tổng tiền trước thuế
tong_tien_truoc_thue = 410000

# Tỷ lệ thuế VAT (10%)
ty_le_thue = 0.10  # 10%

# Tính số tiền thuế
so_tien_thue = tong_tien_truoc_thue * ty_le_thue

# Tính tổng tiền sau thuế
tong_cong_sau_thue = tong_tien_truoc_thue + so_tien_thue

# In kết quả
print(f"Tổng tiền trước thuế: {tong_tien_truoc_thue:.2f} VND")
print(f"Thuế ({ty_le_thue*100}%): {so_tien_thue:.2f} VND")
print(f"Tổng cộng sau thuế: {tong_cong_sau_thue:.2f} VND")