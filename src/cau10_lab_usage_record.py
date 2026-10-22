from datetime import datetime

# 1. Nhập dữ liệu đầu vào
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất thiết bị (W): "))
thoi_gian = float(input("Nhập thời gian sử dụng (phút): "))
don_gia = float(input("Nhập đơn giá điện (VND/kWh): "))

# 2. Tính toán các giá trị (không dùng lệnh if)
dien_nang = (cong_suat * thoi_gian) / 60000
chi_phi = dien_nang * don_gia
tren_60_phut = thoi_gian > 60
thoi_diem = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Xuất kết quả theo định dạng f-string mẫu
print(f"\nMã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat:.2f} W")
print(f"Thời gian: {thoi_gian:.0f} phút")
print(f"Điện năng: {dien_nang:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem}")
Soạn
