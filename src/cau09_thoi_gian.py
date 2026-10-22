from datetime import datetime

# Lấy thời gian hiện tại của hệ thống
thoi_diem = datetime.now()

# Định dạng thời gian thành chuỗi dạng Chuỗi: Năm-Tháng-Ngày Giờ:Phút:Giây
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

# In ra màn hình giá trị và kiểu dữ liệu kiểm tra
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
 
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
