tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Kết quả: {so_gio} giờ và {so_phut_con_lai} phút.")

su_dung_lau = tong_phut > 60
print("Sử dụng lâu:", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# Dự đoán: 
# - Biểu thức 1: Nhân trước cộng sau -> 100 + 20 * 3 = 100 + 60 = 160
# - Biểu thức 2: Thực hiện trong ngoặc trước -> (100 + 20) * 3 = 120 * 3 = 360
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3

print("Kết quả biểu thức 1:", bieu_thuc_1)
print("Kết quả biểu thức 2:", bieu_thuc_2)



