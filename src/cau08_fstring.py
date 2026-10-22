# Cho các biến ban đầu
ma_may = "PC12"
cong_suat_w = 250
dien_nang_kwh = 0.375
chi_phi = 1125

# Dùng f-string để in đúng định dạng mẫu yêu cầu (.2f để lấy 2 chữ số thập phân)
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
