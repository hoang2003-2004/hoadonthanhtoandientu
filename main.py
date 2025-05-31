# Import các lớp và phương thức từ thư viện tkinter
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
from datetime import datetime

if not os.path.exists('Hóa Đơn'):
        os.mkdir('Hóa Đơn')
def start_timer():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timestartEntry.delete(0, END)
    timestartEntry.insert(0, str(start_time))
    timeEndEntry.delete(0, END)
def stop_timer():
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timeEndEntry.delete(0, END)
    timeEndEntry.insert(0, str(end_time))
def clear():
    cfSuaEntry.delete(0, END)
    caCaoEntry.delete(0, END)
    cfDaEntry.delete(0, END)
    bacXiuEntry.delete(0, END)
    phinSuaDaEntry.delete(0, END)
    phinDenDaEntry.delete(0, END)

    nuocCamEntry.delete(0, END)
    nuocOiEntry.delete(0, END)
    nuocTaoEntry.delete(0, END)
    nuocCaRotEntry.delete(0, END)
    nuocDuaHauEntry.delete(0, END)
    nuocDuaEntry.delete(0, END)

    stBoEntry.delete(0, END)
    stXoaiEntry.delete(0, END)
    stDauEntry.delete(0, END)
    stOiEntry.delete(0, END)
    stChuoiEntry.delete(0, END)
    stNhoEntry.delete(0, END)

    cfSuaEntry.insert(0, 0)
    caCaoEntry.insert(0, 0)
    cfDaEntry.insert(0, 0)
    bacXiuEntry.insert(0, 0)
    phinSuaDaEntry.insert(0, 0)
    phinDenDaEntry.insert(0, 0)

    nuocCamEntry.insert(0,0)
    nuocOiEntry.insert(0,0)
    nuocTaoEntry.insert(0,0)
    nuocCaRotEntry.insert(0,0)
    nuocDuaHauEntry.insert(0,0)
    nuocDuaEntry.insert(0,0)

    stBoEntry.insert(0,0)
    stXoaiEntry.insert(0,0)
    stDauEntry.insert(0,0)
    stOiEntry.insert(0,0)
    stChuoiEntry.insert(0,0)
    stNhoEntry.insert(0,0)

    giaCoffeeEntry.delete(0, END)
    giaNuocUongEntry.delete(0,END)
    giaSinhToEntry.delete(0, END)
    giaThueEntry.delete(0, END)
    textarea.delete(1.0, END)


def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(), nguoinhanEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Lỗi', 'Vui lòng thử lại',parent=root1)
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Lỗi', 'Hóa đơn trống')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1,text = "Người gửi",font=('arial', 16 ,'bold'),bd=2,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=10)

        senderLabel = Label(senderFrame, text="Email gửi", font=('arial', 14, 'bold'))
        senderLabel.grid(row=0, column=0,padx=10,pady=20)
        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row= 0, column = 1, padx = 10, pady = 20)

        passwordLabel = Label(senderFrame, text="Mật Khẩu", font=('arial', 14, 'bold'))
        passwordLabel.grid(row=1, column=0,padx=10,pady=20)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row= 1, column = 1, padx = 10, pady = 20)
    # Người Nhận
        nguoiNhanFrame = LabelFrame(root1, text="Người nhận", font=('arial', 16, 'bold'), bd=2, bg='gray20', fg='white')
        nguoiNhanFrame.grid(row=1, column=0, padx=40, pady=20)

        nguoinhanLabel = Label(nguoiNhanFrame, text="Email nhận:", font=('arial', 14, 'bold'))
        nguoinhanLabel.grid(row=0, column=0, padx=10, pady=20)
        nguoinhanEntry = Entry(nguoiNhanFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        nguoinhanEntry.grid(row=0, column=1, padx=10, pady=5)

        tinNhanLabel = Label(nguoiNhanFrame, text="Lời nhắn:", font=('arial', 14, 'bold'))
        tinNhanLabel.grid(row=1, column=0, padx=10, pady=5)

        email_textarea = Text(nguoiNhanFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=' ,'').replace('-','')
                              .replace('\t\t\t', '\t\t'))
        sendButton = Button(root1, text='GỬI', font=('arial', 14, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2, column=0,pady=20)
        root1.mainloop()
def inHoaDon():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Lỗi', 'Hóa đơn trống')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w',encoding='utf-8').write(textarea.get(1.0, END))
        os.startfile(file, 'print')
def timKiemHD():
    for i in os.listdir('Hóa Đơn/'):
        if i.split('.')[0 ]== maHDEntry.get():
            f=open(f'Hóa Đơn/{i}', 'r',encoding='utf-8')
            textarea.delete(1.0,END)
            for data in f:
                textarea. insert (END, data)
            f.close()
            break
    else:
        messagebox.showerror('Lỗi', 'Số hóa đơn không hợp lệ')
def save_bill():
    global maHD
    result=messagebox.askyesno('Thông báo', 'Bạn có muốn lưu hóa đơn không?')
    if result:
        bill_content=textarea.get(1.0, END)
        file = open(f'Hóa Đơn/{maHD}.txt','w',encoding='utf-8')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'Hóa Đơn {maHD} đã được lưu')
        maHD = random.randint(0, 1000)

maHD = random.randint(0,1000)

def hien_thi_bill():
    if nameEntry.get() == '' or soBanEntry.get() == '':
        messagebox.showerror('Lỗi','Mời nhập Tên và số bàn')
    elif giaCoffeeEntry.get() == '0 VND' and giaNuocUongEntry.get() == '0 VND' and giaSinhToEntry.get() == '0 VND':
        messagebox.showerror('Lỗi', 'Không có sản phẩm nào')
    elif giaCoffeeEntry.get() == '' and giaNuocUongEntry.get() == '' and giaSinhToEntry.get() == '':
        messagebox.showerror('Lỗi', 'Không có sản phẩm nào')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Kính Chào Quý Khách**\n')
        textarea.insert(END, f'\nGiờ vào: {timestartEntry.get()}')
        textarea.insert(END, f'\nGiờ ra: {timeEndEntry.get()}')
        textarea.insert(END,f'\nMã Hóa Đơn: {maHD}')
        textarea.insert(END, f'\nTên Khách Hàng: {nameEntry.get()}')
        textarea.insert(END, f'\nSố Bàn: {soBanEntry.get()}\n')
        textarea.insert(END, f'\n=======================================================\n')
        textarea.insert(END, f'\nSản Phẩm\t\t\tSố Lượng\t\t\tGiá VND')
        textarea.insert(END, f'\n=======================================================\n')
        if cfSuaEntry.get() != '0':
            textarea.insert(END, f'Coffee\t\t\t{cfSuaEntry.get()}\t\t\t{cfSua:,.0f}\n')
        if caCaoEntry.get() != '0':
            textarea.insert(END, f'CaCao\t\t\t{caCaoEntry.get()}\t\t\t{caCao:,.0f}\n')
        if cfDaEntry.get() != '0':
            textarea.insert(END, f'Coffee Đá\t\t\t{cfDaEntry.get()}\t\t\t{cfDa:,.0f}\n')
        if bacXiuEntry.get() != '0':
            textarea.insert(END, f'Bạc Xỉu \t\t\t{caCaoEntry.get()}\t\t\t{bacXiu:,.0f}\n')
        if phinSuaDaEntry.get() != '0':
            textarea.insert(END, f'PHIN Sữa Đá\t\t\t{phinSuaDaEntry.get()}\t\t\t{phinSuaDa:,.0f}\n')
        if phinDenDaEntry.get() != '0':
            textarea.insert(END, f'PHIN Đen Đá\t\t\t{phinDenDaEntry.get()}\t\t\t{phinDenDa:,.0f}\n')
#         hiển thị nước uống--------------------
        if nuocCamEntry.get() != '0':
            textarea.insert(END, f'Nước Cam\t\t\t{nuocCamEntry.get()}\t\t\t{nuocCam:,.0f}\n')
        if nuocOiEntry.get() != '0':
            textarea.insert(END, f'Nước Ổi\t\t\t{nuocOiEntry.get()}\t\t\t{nuocOi:,.0f}\n')
        if nuocTaoEntry.get() != '0':
            textarea.insert(END, f'Nước Táo\t\t\t{nuocTaoEntry.get()}\t\t\t{nuocTao:,.0f}\n')
        if nuocCaRotEntry.get() != '0':
            textarea.insert(END, f'Nước Cà Rốt\t\t\t{nuocCaRotEntry.get()}\t\t\t{nuocCaRot:,.0f}\n')
        if nuocDuaHauEntry.get() != '0':
            textarea.insert(END, f'Nước Dưa Hấu\t\t\t{nuocDuaHauEntry.get()}\t\t\t{nuocDuaHau:,.0f}\n')
        if nuocDuaEntry.get() != '0':
            textarea.insert(END, f'Nước Dứa\t\t\t{nuocDuaEntry.get()}\t\t\t{nuocDua:,.0f}\n')

#------------------------------ In Sinh Tố--------------------
        if stBoEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Bơ\t\t\t{stBoEntry.get()}\t\t\t{stBo:,.0f}\n')
        if stXoaiEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Xoài\t\t\t{stXoaiEntry.get()}\t\t\t{stXoai:,.0f}\n')
        if stDauEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Dâu\t\t\t{stDauEntry.get()}\t\t\t{stDau:,.0f}\n')
        if stOiEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Ổi\t\t\t{stOiEntry.get()}\t\t\t{stOi:,.0f}\n')
        if stChuoiEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Chuối\t\t\t{stChuoiEntry.get()}\t\t\t{stChuoi:,.0f}\n')
        if stNhoEntry.get() != '0':
            textarea.insert(END, f'Sinh Tố Nho\t\t\t{stNhoEntry.get()}\t\t\t{stNho:,.0f}\n')


        textarea.insert(END, f'\n-------------------------------------------------------\n')
        if giaThueEntry.get() != '0':
            textarea.insert(END, f'Thuế VAT :)\t\t\t    {giaThue:,.0f} \n')

        if giaThueEntry.get() != '0':
             textarea.insert(END, f'Tổng(bao gồm thuế VAT :)\t\t\t{tong:,.0f}\n ')
        textarea.insert(END, f'\n-------------------------------------------------------')
        save_bill()

# -----------------------------------hàm tính tổng-----------------------------
def tinhTong():
    global cfSua,caCao,cfDa,bacXiu,phinSuaDa,phinDenDa
    global nuocCam,nuocOi,nuocTao,nuocCaRot,nuocDuaHau,nuocDua
    global stBo,stXoai,stDau,stOi,stChuoi,stNho
    global tong,giaThue
#--------------------------------- Tinh TỔng Coffee--------------------------
    cfSua = int(cfSuaEntry.get()) * 20000
    caCao = int(caCaoEntry.get()) * 25000
    cfDa = int(cfDaEntry.get()) * 25000
    bacXiu = int(bacXiuEntry.get()) * 20000
    phinSuaDa = int(phinSuaDaEntry.get()) * 18000
    phinDenDa = int(phinDenDaEntry.get()) * 18000

    giaTongCF = (cfSua +caCao +cfDa+bacXiu+phinSuaDa+ phinDenDa)
    giaCoffeeEntry.delete(0, END)
    giaCoffeeEntry.insert(0,f'{giaTongCF:,.0f} VND')

#    ------------------------------- Tính Tổng Nước uống-----------------------
    nuocCam = int(nuocCamEntry.get()) * 15000
    nuocOi = int(nuocOiEntry.get()) * 15000
    nuocTao = int(nuocTaoEntry.get()) * 15000
    nuocCaRot = int(nuocCaRotEntry.get()) * 20000
    nuocDuaHau = int(nuocDuaHauEntry.get()) * 18000
    nuocDua = int(nuocDuaEntry.get()) * 15000

    giaTongNuocUong = (nuocCam +nuocOi +nuocTao+nuocCaRot+nuocDuaHau+ nuocDua)
    giaNuocUongEntry.delete(0,END)
    giaNuocUongEntry.insert(0,f'{giaTongNuocUong:,.0f} VND')

 #     ---------------------------------Tính Tổng Sinh Tố--------------------------------------
    stBo = int(stBoEntry.get()) * 15000
    stXoai = int(stXoaiEntry.get()) * 15000
    stDau = int(stDauEntry.get()) * 15000
    stOi = int(stOiEntry.get()) * 20000
    stChuoi = int(stChuoiEntry.get()) * 18000
    stNho = int(stNhoEntry.get()) * 15000

    giaTongSinhTo = (stBo + stXoai+ stDau+ stOi + stChuoi + stNho)
    giaSinhToEntry.delete(0, END)
    giaSinhToEntry.insert(0, f'{giaTongSinhTo:,.0f} VND')
 # ------------------------Tính giá thuế--------------------------------------
    giaThue = (giaTongCF + giaTongNuocUong + giaTongSinhTo ) * 0.01
    giaThueEntry.delete(0,END)
    giaThueEntry.insert(0, f'{giaThue:,.0f} VND')

    tong = giaTongCF + giaTongNuocUong + giaTongSinhTo + giaThue


# Tạo cửa sổ gốc (root window)
root = Tk()
# Đặt tiêu đề cho cửa sổ
root.title("Hóa đơn thanh toán")
# Đặt kích thước cho cửa sổ (1270x600 pixel)
root.geometry('1360x760')
mau_nen = "green"

# Đặt biểu tượng cho cửa sổ
root.iconbitmap('icon.ico')
# Tạo nhãn (Label) cho tiêu đề của hóa đơn
headingLabel = Label(root, text='Hóa Đơn Thanh Toán', font=('times new roman', 23, 'bold'),
                     background=mau_nen, fg='gold', bd='8', relief=GROOVE)
# Hiển thị nhãn trên cửa sổ và căn giữa theo chiều ngang (fill=X)
headingLabel.pack(fill=X)

# phần thông tin khách hàng
ThongTinKhachHang = LabelFrame(root, text='ThôngTinKhachHang', font=('times new roman', 15, 'bold'),
                               fg='gold', bd=6, relief=GROOVE, bg=mau_nen)
ThongTinKhachHang.pack(fill=X)

# Phần name
nameLabel = Label(ThongTinKhachHang, text='Tên', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
nameLabel.grid(row=0, column=0, padx=28, pady=2)
nameEntry = Entry(ThongTinKhachHang, font=('arial', 15), bd=6, width=20)
nameEntry.grid(row=0, column=1, padx=18)

# phần soBan
soBanLabel = Label(ThongTinKhachHang, text='Số Bàn', font=('times new roman', 15, 'bold'), bg=mau_nen,
                   fg='white')
soBanLabel.grid(row=0, column=2, padx=28, pady=2)
soBanEntry = Entry(ThongTinKhachHang, font=('arial', 15), bd=6, width=20)
soBanEntry.grid(row=0, column=3, padx=18)

# phần maHD
maHDLabel = Label(ThongTinKhachHang, text='MÃ HD', font=('times new roman', 15, 'bold'), bg=mau_nen,
                  fg='white')
maHDLabel.grid(row=0, column=4, padx=28, pady=2)
maHDEntry = Entry(ThongTinKhachHang, font=('arial', 15), bd=6, width=20)
maHDEntry.grid(row=0, column=5, padx=18)



# nút search
searchButton = Button(ThongTinKhachHang, text='Tìm Kiếm', font=('arial', 12, 'bold'), bd='7',command=timKiemHD)
searchButton.grid(row=0, column=6, padx=70, )

# //////////////////////////////////////////////////////////////////////////////////////////////////
# ------------------------------------------------phần COFFEE----------------------------------------------
productsFrame = Frame(root)
productsFrame.pack()
cosmeticsFrame = LabelFrame(productsFrame, text='COFFEE', font=('times new roman', 15, 'bold'), fg='gold', bd=8,
                            relief=GROOVE, bg=mau_nen)
cosmeticsFrame.grid(row=0, column=0)

# phần cf
cfSuaLabel = Label(cosmeticsFrame, text='Cà phê sữa', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
cfSuaLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
cfSuaEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cfSuaEntry.grid(row=0, column=1, pady=6, padx=10)
cfSuaEntry.insert(0,0)
#
caCaoLabel = Label(cosmeticsFrame, text='Cacao', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
caCaoLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
caCaoEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
caCaoEntry.grid(row=1, column=1, pady=6, padx=10)
caCaoEntry.insert(0,0)
#
cfDaLabel = Label(cosmeticsFrame, text='Cà phê đá ', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
cfDaLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
cfDaEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cfDaEntry.grid(row=2, column=1, pady=6, padx=10)
cfDaEntry.insert(0,0)
#
bacXiuLabel = Label(cosmeticsFrame, text='Bạc Xỉu', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
bacXiuLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
bacXiuEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bacXiuEntry.grid(row=3, column=1, pady=6, padx=10)
bacXiuEntry.insert(0,0)
#
phinSuaDaLabel = Label(cosmeticsFrame, text='PHIN sữa đá', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
phinSuaDaLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
phinSuaDaEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
phinSuaDaEntry.grid(row=4, column=1, pady=6, padx=10)
phinSuaDaEntry.insert(0,0)
#
phinDenDaLabel = Label(cosmeticsFrame, text='PHIN đen đá', font=('times new roman', 15, 'bold'), bg=mau_nen,
                           fg='white')
phinDenDaLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
phinDenDaEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
phinDenDaEntry.grid(row=5, column=1, pady=6, padx=10)
phinDenDaEntry.insert(0,0)


# //////////////////////////////////////////////////////////////////////////////////////////////////
# --------------------------------------------PHẦN Đồ Uống----------------------------------------------
nuocTraiCay = LabelFrame(productsFrame, text='Đồ Uống', font=('times new roman', 15, 'bold'),
                         fg='gold', bd=8, relief=GROOVE, bg=mau_nen)
nuocTraiCay.grid(row=0, column=2)
#
nuocCamLabel = Label(nuocTraiCay, text='Nước Cam', font=('times new roman', 15, 'bold'), bg=mau_nen,
                     fg='white')
nuocCamLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
nuocCamEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocCamEntry.grid(row=0, column=1, pady=6, padx=10)
nuocCamEntry.insert(0,0)
#
nuocOiLabel = Label(nuocTraiCay, text='Nước Ổi', font=('times new roman', 15, 'bold'), bg=mau_nen,
                    fg='white')
nuocOiLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
nuocOiEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocOiEntry.grid(row=1, column=1, pady=6, padx=10)
nuocOiEntry.insert(0,0)
#
nuocTaoLabel = Label(nuocTraiCay, text='Nước Táo', font=('times new roman', 15, 'bold'), bg=mau_nen,
                     fg='white')
nuocTaoLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
nuocTaoEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocTaoEntry.grid(row=2, column=1, pady=6, padx=10)
nuocTaoEntry.insert(0,0)
#
nuocCaRotLabel = Label(nuocTraiCay, text='Nước Cà-rốt', font=('times new roman', 15, 'bold'), bg=mau_nen,
                       fg='white')
nuocCaRotLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
nuocCaRotEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocCaRotEntry.grid(row=3, column=1, pady=6, padx=10)
nuocCaRotEntry.insert(0,0)
#
nuocDuaHauLabel = Label(nuocTraiCay, text='Nước Dưa Hấu', font=('times new roman', 15, 'bold'), bg=mau_nen,
                        fg='white')
nuocDuaHauLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
nuocDuaHauEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocDuaHauEntry.grid(row=4, column=1, pady=6, padx=10)
nuocDuaHauEntry.insert(0,0)
#
nuocDuaLabel = Label(nuocTraiCay, text='Nước Dứa', font=('times new roman', 15, 'bold'), bg=mau_nen,
                     fg='white')
nuocDuaLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
nuocDuaEntry = Entry(nuocTraiCay, font=('times new roman', 15, 'bold'), width=10, bd=5)
nuocDuaEntry.grid(row=5, column=1, pady=6, padx=10)
nuocDuaEntry.insert(0,0)

# //////////////////////////////////////////////////////////////////////////////////////////////////
# ----------------------------------------------PHẦN SINH TỐ---------------------------------------
sinhTo = LabelFrame(productsFrame, text='SINH TỐ', font=('times new roman', 15, 'bold'),
                    fg='gold', bd=8, relief=GROOVE, bg=mau_nen)
sinhTo.grid(row=0, column=3)
#
stBoLabel = Label(sinhTo, text='Sinh Tố Bơ', font=('times new roman', 15, 'bold'), bg=mau_nen,
                  fg='white')
stBoLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
stBoEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stBoEntry.grid(row=0, column=1, pady=6, padx=10)
stBoEntry.insert(0,0)
#
stXoaiLabel = Label(sinhTo, text='Sinh Tố Xoài', font=('times new roman', 15, 'bold'), bg=mau_nen,
                    fg='white')
stXoaiLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
stXoaiEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stXoaiEntry.grid(row=1, column=1, pady=6, padx=10)
stXoaiEntry.insert(0,0)
#
stDauLabel = Label(sinhTo, text='Sinh Tố Dâu', font=('times new roman', 15, 'bold'), bg=mau_nen,
                   fg='white')
stDauLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
stDauEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stDauEntry.grid(row=2, column=1, pady=6, padx=10)
stDauEntry.insert(0,0)
#
stOiLabel = Label(sinhTo, text='Sinh Tố Ổi', font=('times new roman', 15, 'bold'), bg=mau_nen,
                  fg='white')
stOiLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
stOiEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stOiEntry.grid(row=3, column=1, pady=6, padx=10)
stOiEntry.insert(0,0)
#
stChuoiLabel = Label(sinhTo, text='Sinh Tố Chuối', font=('times new roman', 15, 'bold'), bg=mau_nen,
                     fg='white')
stChuoiLabel.grid(row=4, column=0, pady=6, padx=10, sticky='w')
stChuoiEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stChuoiEntry.grid(row=4, column=1, pady=6, padx=10)
stChuoiEntry.insert(0,0)
#
stNhoLabel = Label(sinhTo, text='Sinh Tố Nho', font=('times new roman', 15, 'bold'), bg=mau_nen,
                   fg='white')
stNhoLabel.grid(row=5, column=0, pady=6, padx=10, sticky='w')
stNhoEntry = Entry(sinhTo, font=('times new roman', 15, 'bold'), width=10, bd=5)
stNhoEntry.grid(row=5, column=1, pady=6, padx=10)
stNhoEntry.insert(0,0)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# -----------------------------------PHẦN HIỂN THỊ---------------------------------
billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=4, padx=10)
billareaLabel = Label(billframe, text='Thông Tin Hóa Đơn', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)
# tạo thanh cuộn
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=17, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# ///////////////////////////////////////////////////////////////////////////////////////////
# ----------------------PHẦN CUỐI-------------------------
billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'),
                           fg='gold', bd=6, relief=GROOVE, bg=mau_nen)
billmenuFrame.pack(fill=X)
#
giaCoffeeLabel = Label(billmenuFrame, text='Giá Coffee', font=('times new roman', 15, 'bold'), bg=mau_nen,
                           fg='white')
giaCoffeeLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
giaCoffeeEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
giaCoffeeEntry.grid(row=0, column=1, pady=6, padx=10)
#
giaNuocUongLabel = Label(billmenuFrame, text='Giá Nước Uống', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
giaNuocUongLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
giaNuocUongEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
giaNuocUongEntry.grid(row=1, column=1, pady=6, padx=10)
#
giaSinhToLabel = Label(billmenuFrame, text='Giá Sinh Tố', font=('times new roman', 15, 'bold'), bg=mau_nen, fg='white')
giaSinhToLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
giaSinhToEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
giaSinhToEntry.grid(row=2, column=1, pady=6, padx=10)
# ///////////////////////////
giaThueLabel = Label(billmenuFrame, text='Thuế VAT', font=('times new roman', 15, 'bold'), bg=mau_nen,fg='white')
giaThueLabel.grid(row=3, column=0, pady=6, padx=10, sticky='w')
giaThueEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=15, bd=5)
giaThueEntry.grid(row=3, column=1, pady=6, padx=10)
#

# ----------------------------------------------------TẠO NÚT-------------------------------------------
buttonFrame = Frame(billmenuFrame, bd=12, relief=GROOVE, )
buttonFrame.grid(row=0, column=2, rowspan=4,pady=10)
#
tongButton = Button(buttonFrame, text='Tổng', font=('arial', 16, 'bold'), bg=mau_nen, fg='white', bd=5, width=8,command=tinhTong)
tongButton.grid(row=1, column=0, pady=55, padx=3)

hoaDonButton = Button(buttonFrame, text='Hóa Đơn', font=('arial', 16, 'bold'), bg=mau_nen, fg='white', bd=5, width=8,command=hien_thi_bill)
hoaDonButton.grid(row=1, column=1, pady=55, padx=3)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg=mau_nen, fg='white', bd=5, width=8,command=send_email)
emailButton.grid(row=1, column=2, pady=55, padx=3)

inHDButton = Button(buttonFrame, text='In Bill', font=('arial', 16, 'bold'), bg=mau_nen, fg='white', bd=5, width=8,command=inHoaDon)
inHDButton.grid(row=1, column=3, pady=55, padx=0)

clearButton = Button(buttonFrame, text='Đóng', font=('arial', 16, 'bold'), bg=mau_nen, fg='white', bd=5, width=8,command=clear)
clearButton.grid(row=1, column=4, pady=40, padx=3)
# -------------------------------------------------phần thời gian--------------------------------------
timeFrame = Frame(billmenuFrame, bd=12, relief=GROOVE, )
timeFrame.grid(row=0, column=3, rowspan=4,pady=10,padx=1)

timestartButton = Button(timeFrame, text='Giờ vào', font=('arial', 14, 'bold'), fg='white',bg=mau_nen, bd=4, width=6,command=start_timer)
timestartButton.grid(row=0, column=2, pady=0, padx=0)
timestartEntry = Entry(timeFrame, font=('times new roman', 15, 'bold'), width=18, bd=3)
timestartEntry.grid(row=0, column=1, pady=24, padx=20)

timesEndButton = Button(timeFrame, text='Giờ ra', font=('arial', 14, 'bold'), fg='white', bg=mau_nen,bd=4, width=6,command=stop_timer)
timesEndButton.grid(row=1, column=2, pady=0, padx=0)
timeEndEntry = Entry(timeFrame, font=('times new roman', 15, 'bold'), width=18, bd=3)
timeEndEntry.grid(row=1, column=1, pady=24, padx=20)


root.mainloop()
