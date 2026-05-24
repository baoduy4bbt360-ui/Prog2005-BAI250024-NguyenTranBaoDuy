# Bài 2 Yêu cầu: Tìm số lớn nhất trong ba số. Nhập ba số và in ra số lớn nhất
print("Bai 2")
a= int(input("nhap a: "))
b= int(input("nhap b: "))
c= int(input("nhap c: "))

def add(a, b, c):
    if a > b > c and a>c:
        return print("So lon nhat la a")
    elif a<b and a < c < b:
        return print("So lon nhat la b")
    elif b > a > c and c<b:
            return print("So lon nhat la b")
    elif a>b and a > c > b:
         return print('So lon nhat la a')
    elif a<c and c > b > a:
         return print("So lon nhat la c")
    elif c > a > b and b<c:
        return print("So lon nhat la c")
print(add(a, b, c))

