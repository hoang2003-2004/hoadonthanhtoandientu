from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

def xuat_hoa_don(danh_sach_san_pham, ty_le_vat=0.1, ty_le_chiet_khau=0):
    """
    Tính toán tổng tiền, VAT, chiết khấu và chuẩn bị dữ liệu cho hóa đơn.

    Args:
        danh_sach_san_pham (list): Danh sách sản phẩm (dictionary với 'ten', 'so_luong', 'don_gia').
        ty_le_vat (float): Tỷ lệ VAT (ví dụ: 0.1 cho 10%). Mặc định là 0.1.
        ty_le_chiet_khau (float): Tỷ lệ chiết khấu (ví dụ: 0.05 cho 5%). Mặc định là 0.

    Returns:
        tuple: (tong_tien_hang, tien_chiet_khau, tien_sau_chiet_khau, tien_vat, tong_tien_thanh_toan, data_bang, thong_tin_thanh_toan)
    """
    tong_tien_hang = 0
    data_bang = [['Tên sản phẩm', 'Số lượng', 'Đơn giá', 'Thành tiền']]
    for sp in danh_sach_san_pham:
        thanh_tien = sp['so_luong'] * sp['don_gia']
        tong_tien_hang += thanh_tien
        data_bang.append([
            sp['ten'],
            sp['so_luong'],
            f"{sp['don_gia']:.2f}",
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
        ['Tổng tiền thanh toán:', f'{tong_tien_thanh_toan:.2f}'],
    ]

    return (tong_tien_hang, tien_chiet_khau, tien_sau_chiet_khau, tien_vat, tong_tien_thanh_toan, data_bang, thong_tin_thanh_toan)


def tao_pdf_hoa_don(duong_dan_file, data_bang, thong_tin_thanh_toan):
    doc = SimpleDocTemplate(duong_dan_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>HÓA ĐƠN BÁN HÀNG</b>", styles['Title']))
    elements.append(Spacer(1, 0.2 * inch))

    table_sp = Table(data_bang, colWidths=[3*inch, inch, inch, inch])
    table_sp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    elements.append(table_sp)
    elements.append(Spacer(1, 0.3 * inch))

    table_tt = Table(thong_tin_thanh_toan, colWidths=[4*inch, 2*inch])
    table_tt.setStyle(TableStyle([
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('FONTNAME', (0,-1), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,-1), (1,-1), 'Helvetica-Bold'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(table_tt)

    doc.build(elements)


if __name__ == "__main__":
    danh_sach_mua = [
        {'ten': 'Sản phẩm Alpha', 'so_luong': 3, 'don_gia': 15000},
        {'ten': 'Sản phẩm Beta', 'so_luong': 2, 'don_gia': 25000},
        {'ten': 'Sản phẩm Gamma', 'so_luong': 1, 'don_gia': 50000}
    ]

    tong_tien, chiet_khau, sau_chiet_khau, vat, thanh_toan, bang_data, thong_tin_tt = xuat_hoa_don(
        danh_sach_mua, ty_le_vat=0.08, ty_le_chiet_khau=0.05
    )

    print("--- Thông tin hóa đơn ---")
    print(f"Tổng tiền hàng: {tong_tien:.2f}")
    print(f"Chiết khấu (5%): {chiet_khau:.2f}")
    print(f"Tiền sau chiết khấu: {sau_chiet_khau:.2f}")
    print(f"VAT (8%): {vat:.2f}")
    print(f"Tổng tiền thanh toán: {thanh_toan:.2f}")
    print("------------------------")

    duong_dan_pdf = "hoa_don_chi_tiet.pdf"
    tao_pdf_hoa_don(duong_dan_pdf, bang_data, thong_tin_tt)
    print(f"Hóa đơn chi tiết đã được xuất ra file: {duong_dan_pdf}")

    # Ví dụ với VAT và chiết khấu mặc định
    tong_tien_mac_dinh, _, _, _, thanh_toan_mac_dinh, bang_data_mac_dinh, thong_tin_tt_mac_dinh = xuat_hoa_don(danh_sach_mua)
    duong_dan_pdf_mac_dinh = "hoa_don_mac_dinh.pdf"
    tao_pdf_hoa_don(duong_dan_pdf_mac_dinh, bang_data_mac_dinh, thong_tin_tt_mac_dinh)
    print(f"Hóa đơn mặc định đã được xuất ra file: {duong_dan_pdf_mac_dinh}")