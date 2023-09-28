import numpy as np
from scipy.optimize import linprog

# Nhập số biến và số ràng buộc
num_variables = int(input("Nhập số biến: "))
num_constraints = int(input("Nhập số ràng buộc: "))

# Nhập hệ số của hàm mục tiêu
print("Nhập hệ số của hàm mục tiêu (c):")
c = np.array([float(input(f"c[{i+1}]: ")) for i in range(num_variables)])

# Nhập dấu của hàm ràng buộc (<= hoặc >=)
print("Nhập dấu của hàm ràng buộc (<= hoặc >=) (ví dụ: '<=', '>=', '>=', ...):")
constraint_signs = [input(f"Ràng buộc {i+1}: ") for i in range(num_constraints)]

# Khởi tạo ma trận hệ số A và vector b cho các ràng buộc
A = np.zeros((num_constraints, num_variables))
b = np.zeros(num_constraints)

# Nhập ma trận hệ số A và vector b
print("Nhập ma trận hệ số A:")
for i in range(num_constraints):
    A[i] = [float(x) for x in input().split()]

print("Nhập vector b:")
b = np.array([float(x) for x in input().split()])

# Đưa hàm mục tiêu về dạng tối ưu hóa
if all(sign == '<=' for sign in constraint_signs):
    # Dấu của tất cả ràng buộc là <=, không cần thay đổi
    pass
elif all(sign == '>=' for sign in constraint_signs):
    # Dấu của tất cả ràng buộc là >=, đổi dấu của hàm mục tiêu
    c = -c
else:
    # Trường hợp khác, không thể giải bằng đơn hình
    print("Chương trình chỉ hỗ trợ ràng buộc toàn bộ là '<=' hoặc '>='.")
    exit()

# Giải bài toán LP
result = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * num_variables, method='highs')

# In kết quả
print("Biến tối ưu x:", result.x)
print("Giá trị tối ưu z:", result.fun)
