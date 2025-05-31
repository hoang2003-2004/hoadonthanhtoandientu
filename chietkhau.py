# Tổng tiền ban đầu (sau khi đã tính thuế)
tong_tien_ban_dau = 451000  # Ví dụ

# Tỷ lệ chiết khấu (5%)
ty_le_chiet_khau = 0.05  # 5%

# Tính số tiền chiết khấu
so_tien_chiet_khau = tong_tien_ban_dau * ty_le_chiet_khau

# Tính tổng tiền sau khi áp dụng chiết khấu
tong_tien_sau_chiet_khau = tong_tien_ban_dau - so_tien_chiet_khau

# In kết quả
print(f"Tổng tiền ban đầu: {tong_tien_ban_dau:,.0f} VND")
print(f"Chiết khấu ({ty_le_chiet_khau*100:.0f}%): {so_tien_chiet_khau:,.0f} VND")
print(f"Tổng tiền sau chiết khấu: {tong_tien_sau_chiet_khau:,.0f} VND")