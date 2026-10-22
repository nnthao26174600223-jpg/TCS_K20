# Nhập dữ liệu và chuyển đổi kiểu trực tiếp
ma_may = input("Mã máy: ")
cong_suat_w = float(input("Công suất W: "))
so_phut = int(input("Số phút: "))
don_gia_kwh = float(input("Đơn giá: "))

# Kiểm tra kiểu dữ liệu nhanh
print(type(ma_may), type(cong_suat_w), type(so_phut), type(don_gia_kwh))
# Tính toán và in kết quả
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng:", dien_nang_kwh)
print("Chi phí:", chi_phi)
