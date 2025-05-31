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

def tao_pdf_hoa_don(duong_dan_file, data_bang, thong_tin_thanh_toan):
    """
    Tạo file PDF hóa đơn từ dữ liệu đã tính toán.

    Args:
        duong_dan_file (str): Đường dẫn để lưu file PDF.
        data_bang (list): Dữ liệu cho bảng thông tin sản phẩm.
        thong_tin_thanh_toan (list): Dữ liệu cho bảng thông tin thanh toán.
    """
    doc = SimpleDocTemplate(duong_dan_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Tiêu đề hóa đơn
    elements.append(Paragraph("<b>HÓA ĐƠN BÁN HÀNG</b>", styles['Title']))
    elements.append(Spacer(1, 0.2*inch))

    # Bảng thông tin sản phẩm
    table_san_pham = Table(data_bang, colWidths=[3*inch, inch, inch, inch])
    table_san_pham.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table_san_pham)
    elements.append(Spacer(1, 0.3*inch))

    # Bảng thông tin thanh toán
    table_thanh_toan = Table(thong_tin_thanh_toan, colWidths=[4*inch, 2*inch])
    table_thanh_toan.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, -1), (1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(table_thanh_toan)

    # Tạo file PDF
    doc.build(elements)

# Ví dụ sử dụng:
if __name__ == "__main__":
    danh_sach = [
        {'ten': 'Bút bi', 'so_luong': 10, 'don_gia': 2000},
        {'ten': 'Vở kẻ ngang', 'so_luong': 5, 'don_gia': 12000},
        {'ten': 'Thước kẻ', 'so_luong': 2, 'don_gia': 15000},
    ]

    ket_qua = xuat_hoa_don(danh_sach, ty_le_vat=0.1, ty_le_chiet_khau=0.05)
    (tong_tien_hang, tien_chiet_khau, tien_sau_chiet_khau, tien_vat, tong_tien_thanh_toan, data_bang, thong_tin_thanh_toan) = ket_qua

    duong_dan_file = "hoa_don_ban_hang.pdf"
    tao_pdf_hoa_don(duong_dan_file, data_bang, thong_tin_thanh_toan)
    print(f"Đã tạo file hóa đơn tại: {duong_dan_file}")