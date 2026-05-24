# Bài 7 Yêu cầu: Tính BMI (Chỉ số khối cơ thể)
#Viết một chương trình tính và hiển thị BMI:Nhập cân nặng (kg) và chiều cao (m)
 #Công thức: BMI = weight / (height * height), sử dụng kiểu float và các toán tử số học. Hiển thị BMI làm tròn 2 chữ số thập phân
#Ví dụ: nếu weight = 60kg và height = 1.65m → BMI ≈ 22.04
print("Bai 7")
print("De tinh BMI vui long nhap")
a=float(input("Nhap can nang (KG): "))
b= float(input("Nhap chieu cao (m): "))
bmi= a/(b*b)
print(f"Chi so BMI cua ban la:{round(bmi,2)}")