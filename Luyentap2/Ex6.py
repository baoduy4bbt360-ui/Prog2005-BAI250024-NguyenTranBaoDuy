# Bài 6 Yêu cầu: Chuyển độ C sang độ F Viết một chương trình chuyển nhiệt độ từ độ C sang độ F.
# Yêu cầu người dùng nhập nhiệt độ theo độ C
#(kiểu float). Sử dụng công thức: F = C × 9/5 + 32. In kết quả ra dạng chuỗi định dạng.
print("Bai 6")
c=float(input("Nhap nhiet do C: "))
f= c* (9/5) +32
dof=str(f)
print(f"Nhiet theo thang F la:{dof}")
