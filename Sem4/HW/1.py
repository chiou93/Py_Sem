# 1. Вычислить число c заданной точностью d

num = float(input("Enter the number: "))

_, accu = input("Enter the accuracy '0.0001': ").split(".")
print(f"{num:.{accu}f}")



