# Bài 3 Yêu cầu: Hàm với đối số mặc định Viết một hàm greet(name="Student") in ra “Hello, Student!”. Gọi hàm có và không có đối số
print("Bai 3")
def great(name="Student", ten=0 ):
    print(f"Hello, {name}!")
    print(f"Hello, {ten}!")
str = input("Nhap ten ban: ")
great(name="Student", ten=str)

