# Bài 1 Yêu cầu: Kiểm tra một số chẵn. Viết một hàm is_even(n) trả về True nếu n là số chẵn, ngược lại trả về False.
print("Bai 1")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
n= int(input("Nhap n: "))
print(is_even(n))
