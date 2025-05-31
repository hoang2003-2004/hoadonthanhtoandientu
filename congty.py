from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

def tao_pdf_hoa_don(duong_dan_file, data_bang, thong_tin_thanh_toan):
    """
    Tạo file PDF hóa đơn từ dữ liệu đã tính toán, có thêm phần thông tin công ty và khách hàng.

    Args:
        duong_dan_file (str): Đường dẫn lưu file PDF.
        data_bang (list): Dữ liệu bảng sản phẩm.
        thong_tin_thanh_toan (list): Dữ liệu bảng thanh toán.
    """
    doc = SimpleDocTemplate(duong_dan_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Thông tin công ty
    thong_tin_cong_ty = [
        "<b>Công ty TNHH ABC</b>",
        "Địa chỉ: Số 123 Đường XYZ, Quận Hoàn Kiếm, Hà Nội",
        "Điện thoại: 024 1234 5678",
        "Email: info@abccompany.com"
    ]
    for info in thong_tin_cong_ty:
        elements.append(Paragraph(info, styles['Normal']))
    elements.append(Spacer(1, 0.2 * inch))

    # Thông tin khách hàng
    thong_tin_khach_hang = [
        "<b>Khách hàng: Nguyễn Văn A</b>",
        "Địa chỉ: Số 456 Đường UVW, Quận Ba Đình, Hà Nội",
        "Mã số thuế: 0123456789"
    ]
    for info in thong_tin_khach_hang:
        elements.append(Paragraph(info, styles['Normal']))
    elements.append(Spacer(1, 0.2 * inch))

    # Tiêu đề hóa đơn
    elements.append(Paragraph("<b>HÓA ĐƠN BÁN HÀNG</b>", styles['Title']))
    elements.append(Spacer(1, 0.2 * inch))

    # Bảng thông tin sản phẩm
    table_san_pham = Table(data_bang, colWidths=[3 * inch, inch, inch, inch])
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
    elements.append(Spacer(1, 0.3 * inch))

    # Bảng thông tin thanh toán
    table_thanh_toan = Table(thong_tin_thanh_toan, colWidths=[4 * inch, 2 * inch])
    table_thanh_toan.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, -1), (1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(table_thanh_toan)

    doc.build(elements)

# Phần còn lại (hàm xuat_hoa_don, ví dụ sử dụng) vẫn giữ nguyên như trước đó.