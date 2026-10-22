ma_may = input("Nhập mã máy: ")       #(Sai cú pháp dấu gán): Cụm ma_may ≃ input(...) chứa ký tự lạ ≃ thay vì dấu bằng =
cong_suat_w = float(input("Nhập công suất W: "))      #(Thiếu ép kiểu dữ liệu): Câu lệnh cong_suat_w = input(...) không có hàm float(). Dữ liệu nhập vào sẽ ở dạng chuỗi (str), dẫn đến lỗi khi thực hiện phép tính nhân chia ở các bước sau
so_phut = int(input("Nhập số phút: "))  #(Dư thừa dấu đóng ngoặc): Câu lệnh so_phut = int(input("Nhập số phút: ")) bị dư một dấu đóng ngoặc ) ở cuối cùng ("Nhập số phút: ")))), gây ra lỗi SyntaxError

# Thêm phần tính toán để kiểm tra dữ liệu đầu vào đã hoạt động chuẩn xác
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
