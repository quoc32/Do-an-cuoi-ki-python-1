import tkinter as tk

# Tạo một cửa sổ Tkinter
root = tk.Tk()
root.title("Ví dụ về Canvas")

# Tạo một Canvas
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Vẽ một số hình dạng trên Canvas
canvas.create_rectangle(50, 50, 150, 100, fill='blue', outline='black')  # Hình chữ nhật
canvas.create_oval(200, 50, 300, 150, fill='red', outline='black')      # Hình tròn
canvas.create_line(0, 0, 400, 400, fill='green', width=3)              # Đường thẳng

# Chèn một hình ảnh (giả sử bạn có file hình ảnh 'image.png' trong cùng thư mục)
# img = tk.PhotoImage(file='image.png')
# canvas.create_image(200, 200, anchor=tk.CENTER, image=img)

# Chạy vòng lặp chính
root.mainloop()

