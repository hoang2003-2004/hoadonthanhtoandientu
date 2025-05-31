def xuat_hoa_don(danh_sach_san_pham, ty_le_vat=0.1, ty_le_chiet_khau=0):
    """
    Tính toán tổng tiền, VAT, chiết khấu và chuẩn bị dữ liệu cho hóa đơn.

    Args:
        danh_sach_san_pham (list): Danh sách các sản phẩm (dictionary với 'ten', 'so_luong', 'don_gia').
        ty_le_vat (float): Tỷ lệ VAT (ví dụ: 0.1 cho 10%). Mặc định là 0.1.
        ty_le_chiet_khau (float): Tỷ lệ chiết khấu (ví dụ: 0.05 cho 5%). Mặc định là 0.

    Returns:
        tuple: Bao gồm tổng tiền hàng, tiền chiết khấu, tiền sau chiết khấu, tiền VAT, tổng tiền thanh toán,
               dữ liệu bảng sản phẩm và dữ liệu bảng thanh toán.
    """
    tong_tien_hang = 0
    data_bang = [['Tên sản phẩm', 'Số lượng', 'Đơn giá', 'Thành tiền']]
    
    for san_pham in danh_sach_san_pham:
        thanh_tien = san_pham['so_luong'] * san_pham['don_gia']
        tong_tien_hang += thanh_tien
        data_bang.append([
            san_pham['ten'], 
            san_pham['so_luong'], 
            f"{san_pham['don_gia']:.2f}", 
            f"{thanh_tien:.2f}"
        ])

    tien_chiet_khau = tong_tien_hang * ty_le_chiet_khau
    tien_sau_chiet_khau = tong_tien_hang - tien_chiet_khau
    tien_vat = tien_sau_chiet_khau * ty_le_vat
    tong_tien_thanh_toan = tien_sau_chiet_khau + tien_vat

    thong_tin_thanh_toan = [
        ['Tổng tiền hàng:', f'{tong_tien_hang:.2f}'],
        [f'Chiết khấu ({ty_le_chiet_khau*100:.0f}%):', f'{tien_chiet_khau:.2f}'],
        ['Tiền sau chiết khấu:', f'{tien_sau_chiet_khau:.2f}'],
        [f'VAT ({ty_le_vat*100:.0f}%):', f'{tien_vat:.2f}'],
        ['Tổng tiền thanh toán:', f'{tong_tien_thanh_toan:.2f}']
    ]

    return (tong_tien_hang, tien_chiet_khau, tien_sau_chiet_khau, tien_vat, tong_tien_thanh_toan, data_bang, thong_tin_thanh_toan)


# Ví dụ sử dụng hàm
danh_sach = [
    {'ten': 'Bút bi', 'so_luong': 10, 'don_gia': 2000},
    {'ten': 'Vở kẻ ngang', 'so_luong': 5, 'don_gia': 12000},
    {'ten': 'Thước kẻ', 'so_luong': 2, 'don_gia': 15000},
]

ket_qua = xuat_hoa_don(danh_sach, ty_le_vat=0.1, ty_le_chiet_khau=0.05)

(tong_tien_hang, tien_chiet_khau, tien_sau_chiet_khau, tien_vat, tong_tien_thanh_toan, data_bang, thong_tin_thanh_toan) = ket_qua

print("=== Bảng chi tiết sản phẩm ===")
for row in data_bang:
    print("{:<15} {:<10} {:<10} {:<15}".format(*row))

print("\n=== Thông tin thanh toán ===")
for item in thong_tin_thanh_toan:
    print(f"{item[0]:<20} {item[1]:>10}")