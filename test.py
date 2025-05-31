import tkinter as tk
from datetime import datetime

class TimerApp:
    def __init__(self, root):
        # Khởi tạo ứng dụng với cửa sổ root được truyền vào.
        self.root = root
        self.root.title('Đồng hồ đếm thời gian')
        self.start_time = None
        self.end_time = None

        # Tạo và thiết lập các widget trên giao diện người dùng.
        # Tạo ô nhập thời gian bắt đầu và nút bắt đầu.
        self.start_time_entry = tk.Entry(root, font=('calibri', 10), width=20)
        self.start_time_entry.grid(row=0, column=1, padx=5, pady=5)
        self.start_button = tk.Button(root, text='Bắt đầu', command=self.start_timer, font=('calibri', 10))
        self.start_button.grid(row=0, column=2, padx=5, pady=5)

        # Tạo ô nhập thời gian kết thúc và nút kết thúc.
        self.end_time_entry = tk.Entry(root, font=('calibri', 10), width=20)
        self.end_time_entry.grid(row=1, column=1, padx=5, pady=5)
        self.stop_button = tk.Button(root, text='Kết thúc', command=self.stop_timer, font=('calibri', 10))
        self.stop_button.grid(row=1, column=2, padx=5, pady=5)

        # Hiển thị thời gian hiện tại ở giữa giao diện.
        self.label = tk.Label(root, font=('calibri', 10),bg='blue', foreground='white')
        self.label.grid(row=2, column=1, padx=3, pady=5, sticky='we')

        # Cập nhật thời gian hiển thị trên nhãn mỗi giây.
        self.update_time()

    # Hàm bắt đầu đếm thời gian khi nút "Bắt đầu" được nhấn.
    def start_timer(self):
        self.start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.start_time_entry.delete(0, tk.END)
        self.start_time_entry.insert(0, str(self.start_time))
        self.end_time_entry.delete(0, tk.END)

    # Hàm kết thúc đếm thời gian khi nút "Kết thúc" được nhấn.
    def stop_timer(self):
        self.end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.end_time_entry.delete(0, tk.END)
        self.end_time_entry.insert(0, str(self.end_time))

    def update_time(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # self.label.config(text=current_time)
        self.label.after(1000, self.update_time)

# Khởi tạo ứng dụng tkinter và gán nó cho biến root.
root = tk.Tk()
# Tạo một đối tượng TimerApp với cửa sổ root.
app = TimerApp(root)
# Bắt đầu vòng lặp chính của ứng dụng tkinter để hiển thị giao diện người dùng.
root.mainloop()
